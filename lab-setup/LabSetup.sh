#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
MANIFEST="$SCRIPT_DIR/lab-apps.tsv"
WIN_MANIFEST="$SCRIPT_DIR/windows-iis-apps.tsv"
WIN_INSTALLER="$SCRIPT_DIR/Install-WindowsIisTargets.ps1"
ASSET_ROOT="$REPO_ROOT/docker-images/security-testing-lab"
REMOTE_DIR="security-testing-lab"
TAB=$(printf "\t")
MODE="${1:-linux}"

if [[ ! -f "$MANIFEST" ]]; then
  printf "Manifest missing: %s\n" "$MANIFEST" >&2
  exit 1
fi

APP_IDS=()
declare -A APP_NAME APP_HOST APP_URL APP_COMPOSE APP_SERVICE APP_PORT APP_INTERNAL APP_CRED APP_CPU APP_MEM APP_DISK APP_STATUS APP_NOTES APP_SOURCE
while IFS="$TAB" read -r app_id application runtime_host runtime_url source_ref docker_asset compose_ref service default_port internal_port credential_ref min_cpu min_mem min_disk status notes; do
  [[ "$app_id" == "app_id" ]] && continue
  APP_IDS+=("$app_id")
  APP_NAME["$app_id"]="$application"
  APP_HOST["$app_id"]="$runtime_host"
  APP_URL["$app_id"]="$runtime_url"
  APP_SOURCE["$app_id"]="$source_ref"
  APP_COMPOSE["$app_id"]="$compose_ref"
  APP_SERVICE["$app_id"]="$service"
  APP_PORT["$app_id"]="$default_port"
  APP_INTERNAL["$app_id"]="$internal_port"
  APP_CRED["$app_id"]="$credential_ref"
  APP_CPU["$app_id"]="$min_cpu"
  APP_MEM["$app_id"]="$min_mem"
  APP_DISK["$app_id"]="$min_disk"
  APP_STATUS["$app_id"]="$status"
  APP_NOTES["$app_id"]="$notes"
done < "$MANIFEST"

ssh_base() {
  local server="$1"
  shift
  local pass="${SERVER_PASS[$server]:-}"
  if [[ -n "$pass" && -x "$(command -v sshpass || true)" ]]; then
    sshpass -p "$pass" ssh -o StrictHostKeyChecking=accept-new "$server" "$@"
  else
    if [[ -n "$pass" ]]; then
      printf "sshpass is not installed. SSH may prompt interactively for %s.\n" "$server" >&2
    fi
    ssh -o StrictHostKeyChecking=accept-new "$server" "$@"
  fi
}

scp_base() {
  local server="$1"
  local src="$2"
  local dest="$3"
  local pass="${SERVER_PASS[$server]:-}"
  if [[ -n "$pass" && -x "$(command -v sshpass || true)" ]]; then
    sshpass -p "$pass" scp -o StrictHostKeyChecking=accept-new "$src" "$server:$dest"
  else
    if [[ -n "$pass" ]]; then
      printf "sshpass is not installed. SCP may prompt interactively for %s.\n" "$server" >&2
    fi
    scp -o StrictHostKeyChecking=accept-new "$src" "$server:$dest"
  fi
}

prompt_servers() {
  read -r -p "Destination servers, comma-separated user@host or host: " server_line
  server_line=${server_line// /}
  IFS="," read -r -a SERVERS <<< "$server_line"
  if [[ "${#SERVERS[@]}" -eq 0 || -z "${SERVERS[0]}" ]]; then
    printf "No destination servers supplied.\n" >&2
    exit 1
  fi
  declare -gA SERVER_PASS
  for i in "${!SERVERS[@]}"; do
    local server="${SERVERS[$i]}"
    if [[ "$server" != *@* ]]; then
      read -r -p "SSH username for $server: " user
      server="$user@$server"
      SERVERS[$i]="$server"
    fi
    read -r -s -p "SSH password for $server, leave blank for keys or interactive SSH: " pass
    printf "\n"
    SERVER_PASS["$server"]="$pass"
  done
}

select_apps() {
  local desired_status="$1"
  SELECTED=()
  declare -gA IDX_TO_APP
  IDX_TO_APP=()
  local idx=1
  for app_id in "${APP_IDS[@]}"; do
    if [[ "${APP_STATUS[$app_id]}" == "$desired_status" ]]; then
      printf "%3d. %-36s %s [%s]\n" "$idx" "$app_id" "${APP_NAME[$app_id]}" "${APP_HOST[$app_id]}"
      IDX_TO_APP["$idx"]="$app_id"
      idx=$((idx + 1))
    fi
  done
  read -r -p "Select apps by number or app_id, comma-separated, or type all: " selection
  selection=${selection// /}
  if [[ "$selection" == "all" || "$selection" == "ALL" ]]; then
    for app_id in "${APP_IDS[@]}"; do
      [[ "${APP_STATUS[$app_id]}" == "$desired_status" ]] && SELECTED+=("$app_id")
    done
  else
    IFS="," read -r -a parts <<< "$selection"
    for part in "${parts[@]}"; do
      if [[ -n "${IDX_TO_APP[$part]:-}" ]]; then
        SELECTED+=("${IDX_TO_APP[$part]}")
      elif [[ -n "${APP_STATUS[$part]:-}" && "${APP_STATUS[$part]}" == "$desired_status" ]]; then
        SELECTED+=("$part")
      else
        printf "Unknown or unsupported selection for %s mode: %s\n" "$desired_status" "$part" >&2
        exit 1
      fi
    done
  fi
  if [[ "${#SELECTED[@]}" -eq 0 ]]; then
    printf "No applications selected.\n" >&2
    exit 1
  fi
}

sync_assets() {
  local server="$1"
  printf "Syncing docker assets to %s:%s ...\n" "$server" "$REMOTE_DIR"
  tar -C "$ASSET_ROOT" -cz . | ssh_base "$server" "mkdir -p '$REMOTE_DIR' && tar -xzf - -C '$REMOTE_DIR'"
}

used_ports() {
  local server="$1"
  ssh_base "$server" '((ss -ltnH 2>/dev/null || true); docker ps --format "{{.Ports}}" 2>/dev/null || true)' | grep -Eo ':[0-9]+' | tr -d : | sort -n | uniq || true
}

choose_port() {
  local desired="$1"
  local used="$2"
  local port="$desired"
  while grep -qx "$port" <<< "$used"; do
    port=$((port + 1))
  done
  printf "%s" "$port"
}

run_linux() {
  if [[ ! -d "$ASSET_ROOT" ]]; then
    printf "Docker assets missing: %s\nRun the repository asset generation step or restore docker-images/security-testing-lab.\n" "$ASSET_ROOT" >&2
    exit 1
  fi
  printf "SecurityTestingLab Linux Docker lab deployment setup\n"
  printf "No credentials are stored. Password prompts are in-memory for this run only.\n\n"
  printf "Available containerized applications:\n"
  select_apps "containerized"
  local sum_cpu=0 sum_mem=0 sum_disk=0
  for app_id in "${SELECTED[@]}"; do
    sum_cpu=$((sum_cpu + APP_CPU[$app_id]))
    sum_mem=$((sum_mem + APP_MEM[$app_id]))
    sum_disk=$((sum_disk + APP_DISK[$app_id]))
  done
  printf "\nSelected %d apps. Suggested minimum combined capacity: %d vCPU, %d MiB RAM, %d GiB free disk.\n" "${#SELECTED[@]}" "$sum_cpu" "$sum_mem" "$sum_disk"
  prompt_servers
  for server in "${SERVERS[@]}"; do
    printf "\nPreflight %s\n" "$server"
    ssh_base "$server" 'command -v docker >/dev/null && (docker compose version >/dev/null 2>&1 || docker-compose version >/dev/null 2>&1) && nproc && awk "/MemTotal/ {print \$2}" /proc/meminfo && df -BG / | awk "NR==2 {print \$4}"' || {
      printf "Preflight failed for %s. Install Docker Compose and verify SSH credentials.\n" "$server" >&2
      exit 1
    }
    remote_ports=$(used_ports "$server")
    sync_assets "$server"
    for app_id in "${SELECTED[@]}"; do
      desired="${APP_PORT[$app_id]}"
      internal="${APP_INTERNAL[$app_id]}"
      port=$(choose_port "$desired" "$remote_ports")
      remote_ports="$remote_ports
$port"
      compose="${APP_COMPOSE[$app_id]}"
      service="${APP_SERVICE[$app_id]}"
      override="/tmp/securitytestinglab-${app_id}-ports.yml"
      printf "Deploying %s to %s on host port %s -> container port %s\n" "$app_id" "$server" "$port" "$internal"
      ssh_base "$server" "cat > '$override' <<YAML
services:
  $service:
    ports:
      - \"0.0.0.0:$port:$internal\"
YAML
cd '$REMOTE_DIR' && if docker compose version >/dev/null 2>&1; then docker compose -f '$compose' -f '$override' up -d --build '$service'; else docker-compose -f '$compose' -f '$override' up -d --build '$service'; fi"
    done
  done
  printf "\nDeployment requests complete. Review docker compose output on each destination server.\n"
}

run_windows_iis() {
  if [[ ! -f "$WIN_MANIFEST" || ! -f "$WIN_INSTALLER" ]]; then
    printf "Windows IIS manifest or installer missing under lab-setup/.\n" >&2
    exit 1
  fi
  printf "SecurityTestingLab Windows Server/IIS lab deployment setup\n"
  printf "No credentials are stored. Password prompts are in-memory for this run only.\n"
  printf "The remote host must accept SSH and run Windows PowerShell.\n\n"
  printf "Available Windows/IIS applications:\n"
  select_apps "windows-iis"
  prompt_servers
  package_dir=$(mktemp -d)
  archive=$(mktemp --suffix=.tgz)
  mkdir -p "$package_dir/sources"
  cp "$WIN_MANIFEST" "$package_dir/windows-iis-apps.tsv"
  cp "$WIN_INSTALLER" "$package_dir/Install-WindowsIisTargets.ps1"
  for app_id in "${SELECTED[@]}"; do
    src="$REPO_ROOT/${APP_SOURCE[$app_id]}"
    if [[ -d "$src" ]]; then
      cp -a "$src" "$package_dir/sources/$app_id"
    else
      printf "Local source cache missing for %s; remote installer will try public fallback if git is available.\n" "$app_id" >&2
    fi
  done
  tar -C "$package_dir" -czf "$archive" .
  ps_ids=""
  for app_id in "${SELECTED[@]}"; do
    ps_ids+="'$app_id',"
  done
  ps_ids=${ps_ids%,}
  for server in "${SERVERS[@]}"; do
    printf "\nWindows preflight %s\n" "$server"
    ssh_base "$server" 'powershell -NoProfile -Command "$os = Get-CimInstance Win32_OperatingSystem; if ($os.Caption -notmatch '"'"'Windows Server'"'"') { exit 10 }; if ($os.Caption -notmatch '"'"'2019|2022'"'"') { exit 11 }; Write-Output $os.Caption"' || {
      printf "Preflight failed for %s. The target must be Windows Server 2019/2022 and reachable over SSH.\n" "$server" >&2
      exit 1
    }
    ssh_base "$server" 'powershell -NoProfile -Command "New-Item -ItemType Directory -Force -Path SecurityTestingLabWindowsIisTargets | Out-Null"'
    scp_base "$server" "$archive" "SecurityTestingLabWindowsIisTargets/package.tgz"
    ssh_base "$server" 'powershell -NoProfile -Command "tar -xzf SecurityTestingLabWindowsIisTargets/package.tgz -C SecurityTestingLabWindowsIisTargets"'
    ssh_base "$server" "powershell -NoProfile -ExecutionPolicy Bypass -File SecurityTestingLabWindowsIisTargets/Install-WindowsIisTargets.ps1 -ManifestPath SecurityTestingLabWindowsIisTargets/windows-iis-apps.tsv -SourceRoot SecurityTestingLabWindowsIisTargets/sources -AppIds $ps_ids"
  done
  rm -rf "$package_dir" "$archive"
  printf "\nWindows IIS deployment requests complete. Verify URLs with sanitized metadata only.\n"
}

case "$MODE" in
  linux|--linux|"") run_linux ;;
  windows-iis|--windows-iis) run_windows_iis ;;
  --help|-h)
    printf "usage: %s [linux|--linux|windows-iis|--windows-iis]\n" "$0"
    ;;
  *)
    printf "Unknown mode: %s\nusage: %s [linux|--linux|windows-iis|--windows-iis]\n" "$MODE" "$0" >&2
    exit 2
    ;;
esac

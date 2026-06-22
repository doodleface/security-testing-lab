#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
MANIFEST="$ROOT_DIR/manifest.tsv"
APP_ID="${1:-}"
if [[ -z "$APP_ID" ]]; then
  printf "usage: %s <app_id>
" "$0" >&2
  exit 2
fi
TAB=$(printf "	")
found=0
while IFS="$TAB" read -r app_id application runtime_host runtime_url source_ref docker_asset compose_ref service default_port internal_port credential_ref min_cpu min_mem min_disk status notes; do
  [[ "$app_id" == "app_id" ]] && continue
  [[ "$app_id" != "$APP_ID" ]] && continue
  found=1
  if [[ "$status" != "containerized" ]]; then
    printf "%s is not containerized: %s
" "$APP_ID" "$notes" >&2
    exit 1
  fi
  compose_path="$ROOT_DIR/$compose_ref"
  if [[ ! -f "$compose_path" ]]; then
    printf "compose file missing for %s: %s
" "$APP_ID" "$compose_path" >&2
    exit 1
  fi
  override=$(mktemp)
  cat > "$override" <<YAML
services:
  $service:
    ports:
      - "0.0.0.0:${default_port}:${internal_port}"
YAML
  docker compose -f "$compose_path" -f "$override" build "$service" || docker compose -f "$compose_path" -f "$override" pull "$service"
  rm -f "$override"
  exit 0
done < "$MANIFEST"
if [[ "$found" -eq 0 ]]; then
  printf "unknown app_id: %s
" "$APP_ID" >&2
  exit 1
fi

param(
  [Parameter(Mandatory=$true)][string]$ManifestPath,
  [Parameter(Mandatory=$true)][string]$SourceRoot,
  [string[]]$AppIds = @()
)
$ErrorActionPreference = 'Stop'
function Write-Meta($Message) { Write-Host "[SecurityTestingLab-Windows-IIS] $Message" }
$os = Get-CimInstance Win32_OperatingSystem
if ($os.Caption -notmatch 'Windows Server') { throw 'Remote target is not Windows Server.' }
if ($os.Caption -notmatch '2019|2022') { throw "Unsupported Windows Server version: $($os.Caption). Use Windows Server 2019 or 2022." }
Write-Meta "Detected supported $($os.Caption)"
if (Get-Command Get-WindowsFeature -ErrorAction SilentlyContinue) {
  $features = @('Web-Server','Web-Asp-Net45','Web-Mgmt-Tools','Web-WebSockets','Web-Static-Content','Web-Default-Doc')
  foreach ($feature in $features) {
    $state = Get-WindowsFeature -Name $feature -ErrorAction SilentlyContinue
    if ($state -and -not $state.Installed) {
      Write-Meta "Installing Windows feature $feature"
      Install-WindowsFeature -Name $feature -IncludeManagementTools | Out-Null
    }
  }
} else {
  Write-Meta 'Get-WindowsFeature unavailable; skipping automatic IIS feature installation.'
}
if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) {
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Meta 'Installing .NET Hosting Bundle with winget if available.'
    winget install --id Microsoft.DotNet.HostingBundle.8 --silent --accept-package-agreements --accept-source-agreements | Out-Null
  } else {
    Write-Meta '.NET runtime not detected and winget unavailable; install the .NET Hosting Bundle manually if ASP.NET Core hosting is needed.'
  }
}
if (Get-Command winget -ErrorAction SilentlyContinue) {
  Write-Meta 'Checking URL Rewrite availability; attempting safe winget install if package source supports it.'
  winget install --id Microsoft.IIS.URLRewrite --silent --accept-package-agreements --accept-source-agreements 2>$null | Out-Null
}
$dbServices = Get-Service -Name 'MSSQL*','SQL*' -ErrorAction SilentlyContinue
if ($dbServices) {
  Write-Meta 'Database prerequisite check found SQL-family services.'
} else {
  Write-Meta 'Database prerequisite check found no SQL-family service; install SQL Server Express or a supported database if the selected app requires one.'
}
Import-Module WebAdministration -ErrorAction SilentlyContinue
if (-not (Test-Path $ManifestPath)) { throw "Manifest missing: $ManifestPath" }
$rows = Import-Csv -Path $ManifestPath -Delimiter "`t"
if ($AppIds.Count -gt 0) { $rows = $rows | Where-Object { $AppIds -contains $_.app_id } }
New-Item -ItemType Directory -Force -Path 'C:\inetpub\SecurityTestingLab' | Out-Null
foreach ($row in $rows) {
  $source = Join-Path $SourceRoot $row.app_id
  if (-not (Test-Path $source)) {
    if (Get-Command git -ErrorAction SilentlyContinue) {
      Write-Meta "Local source missing for $($row.app_id); cloning public fallback."
      git clone --depth 1 $row.public_repo $source | Out-Null
    } else {
      throw "Local source missing for $($row.app_id) and git unavailable for public fallback."
    }
  }
  $sitePath = $row.default_site_path
  New-Item -ItemType Directory -Force -Path $sitePath | Out-Null
  Copy-Item -Path (Join-Path $source '*') -Destination $sitePath -Recurse -Force
  $poolName = "SecurityTestingLab-$($row.app_id)"
  $siteName = "SecurityTestingLab-$($row.app_id)"
  if (-not (Test-Path "IIS:\AppPools\$poolName")) { New-WebAppPool -Name $poolName | Out-Null }
  if (Test-Path "IIS:\Sites\$siteName") { Remove-Website -Name $siteName }
  New-Website -Name $siteName -PhysicalPath $sitePath -Port ([int]$row.default_port) -ApplicationPool $poolName | Out-Null
  Write-Meta "Installed $($row.app_id) on port $($row.default_port)"
}
Write-Meta 'Windows IIS target installation complete.'

$ErrorActionPreference = "Stop"

$root = "C:\sites\flora-street-strategies"
$envFile = Join-Path $root ".env"

if (Test-Path $envFile) {
  Get-Content $envFile | ForEach-Object {
    if ($_ -match '^(.*?)=(.*)$') {
      [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process')
    }
  }
}

$port = if ($env:STATIC_SITE_PORT) { $env:STATIC_SITE_PORT } else { "8088" }

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
  throw "Docker is not installed or not in PATH. Run scripts/install-prereqs.ps1 first."
}

docker compose -f (Join-Path $root "docker-compose.yml") up -d static-site

docker compose -f (Join-Path $root "docker-compose.yml") ps
Write-Host "Static container started. Test at http://localhost:$port" -ForegroundColor Green

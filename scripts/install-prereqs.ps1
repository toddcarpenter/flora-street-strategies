$ErrorActionPreference = "Stop"

Write-Host "Installing Docker Desktop and cloudflared via winget..." -ForegroundColor Cyan

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  throw "winget is required but was not found. Install App Installer from Microsoft Store first."
}

winget install -e --id Docker.DockerDesktop --accept-source-agreements --accept-package-agreements
winget install -e --id Cloudflare.cloudflared --accept-source-agreements --accept-package-agreements

Write-Host "Installation commands completed." -ForegroundColor Green
Write-Host "Open Docker Desktop once and finish initial setup, then reboot if prompted." -ForegroundColor Yellow

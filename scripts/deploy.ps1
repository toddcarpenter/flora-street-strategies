param(
  [string]$Destination = "C:\sites\toddl.es\site\florastreetstrategies",
  [string]$Version = (Get-Date -Format "yyyyMMddHHmmss")
)

$ErrorActionPreference = "Stop"
$source = Join-Path (Split-Path $PSScriptRoot -Parent) "site"

if (-not (Test-Path -LiteralPath $source -PathType Container)) {
  throw "Site source was not found: $source"
}

if (-not (Test-Path -LiteralPath $Destination -PathType Container)) {
  New-Item -ItemType Directory -Path $Destination -Force | Out-Null
}

Copy-Item -Path (Join-Path $source "*") -Destination $Destination -Recurse -Force

$assetPattern = '(?<prefix>\b(?:href|src)=["''])(?<path>(?!https?:|//|data:|mailto:|tel:|#)[^"'']+?\.(?:css|js|png|jpe?g|gif|webp|svg|ico|woff2?|ttf|otf))(?:\?[^"'']*)?(?<suffix>["''])'
$htmlFiles = Get-ChildItem -LiteralPath $Destination -Filter "*.html" -File -Recurse

foreach ($file in $htmlFiles) {
  $content = [System.IO.File]::ReadAllText($file.FullName)
  $updated = [regex]::Replace($content, $assetPattern, {
    param($match)
    "$($match.Groups['prefix'].Value)$($match.Groups['path'].Value)?v=$Version$($match.Groups['suffix'].Value)"
  }, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

  if ($updated -ne $content) {
    [System.IO.File]::WriteAllText($file.FullName, $updated, [System.Text.UTF8Encoding]::new($false))
  }
}

Write-Host "Deployed $source to $Destination" -ForegroundColor Green
Write-Host "Cache version: $Version" -ForegroundColor Green
Write-Host "Updated HTML files: $($htmlFiles.Count)" -ForegroundColor Green

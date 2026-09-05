# Computational Agent Skills — Universal Installer (Windows PowerShell)
# Copies/links skills to Google Antigravity and Claude Code

param(
    [switch]$Antigravity,
    [switch]$Claude,
    [switch]$All,
    [string]$Workspace = ""
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $PSScriptRoot
$SkillsSrc = Join-Path $ScriptDir "skills"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  ⚡ Computational Agent Skills — Windows Installer" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Source: $SkillsSrc"

function Install-Skills([string]$TargetDir, [string]$PlatformName) {
    if (-not (Test-Path $TargetDir)) {
        New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    }
    Write-Host "`nInstalling into $PlatformName ($TargetDir)..." -ForegroundColor Yellow

    Get-ChildItem -Directory $SkillsSrc | ForEach-Object {
        $skillName = $_.Name
        $dest = Join-Path $TargetDir $skillName
        
        if (Test-Path $dest) {
            Remove-Item $dest -Recurse -Force
        }
        
        # Copy as real directory to prevent nested junction recursion limits
        Copy-Item $_.FullName $dest -Recurse -Force
        Write-Host "  ✓ Installed /$skillName" -ForegroundColor Green
    }
}

# Auto-detect or use flags
$installAll = $All.IsPresent -or (-not $Antigravity.IsPresent -and -not $Claude.IsPresent -and [string]::IsNullOrEmpty($Workspace))

# 1. Google Antigravity
$geminiDir = Join-Path $env:USERPROFILE ".gemini\config\skills"
if ($installAll -or $Antigravity.IsPresent -or (Test-Path (Join-Path $env:USERPROFILE ".gemini"))) {
    Install-Skills $geminiDir "Google Antigravity"
}

# 2. Claude Code
$claudeDir = Join-Path $env:USERPROFILE ".claude\skills"
if ($installAll -or $Claude.IsPresent -or (Test-Path (Join-Path $env:USERPROFILE ".claude"))) {
    Install-Skills $claudeDir "Claude Code"
}

# 3. Workspace
if (-not [string]::IsNullOrEmpty($Workspace) -and (Test-Path $Workspace)) {
    $wsTarget = Join-Path $Workspace ".agents\skills"
    Install-Skills $wsTarget "Workspace ($Workspace)"
}

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "  ✓ Installation Complete! All skills ready to trigger." -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan

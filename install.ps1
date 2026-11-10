# Joe Skills Installer (PowerShell)
$ErrorActionPreference = "Stop"
$src = $PSScriptRoot
$homeDir = $env:USERPROFILE
$configDir = "$homeDir\.config\opencode"
$agentsDir = "$configDir\agents"
$skillsDir = "$configDir\skills"

Write-Host "=== Joe Skills Installer ===" -ForegroundColor Cyan

# 1. Create dirs
New-Item -ItemType Directory -Force -Path $agentsDir | Out-Null
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null

# 2. Copy agents
Copy-Item -Recurse -Force "$src\agents\*" $agentsDir
Write-Host "Agents copied."

# 3. Copy skills
Copy-Item -Recurse -Force "$src\skills\*" $skillsDir
Write-Host "Skills copied."

# 4. Merge config
$configPath = "$configDir\opencode.jsonc"
if (Test-Path $configPath) {
    $cur = Get-Content $configPath -Raw | ConvertFrom-Json
} else {
    $cur = @{}
}
$srcCfg = Get-Content "$src\opencode.jsonc" -Raw | ConvertFrom-Json
if (-not $cur.mcp) { $cur | Add-Member -NotePropertyName mcp -NotePropertyValue @{} -Force }
if (-not $cur.mcp.servers) { $cur.mcp | Add-Member -NotePropertyName servers -NotePropertyValue @{} -Force }
foreach ($k in $srcCfg.mcp.servers.PSObject.Properties.Name) {
    $cur.mcp.servers | Add-Member -NotePropertyName $k -NotePropertyValue $srcCfg.mcp.servers.$k -Force
}
if ($srcCfg.default_agent) { $cur.default_agent = $srcCfg.default_agent }
if ($srcCfg.model) { $cur.model = $srcCfg.model }
$cur | ConvertTo-Json -Depth 10 | Set-Content $configPath -Encoding UTF8
Write-Host "Config merged."

# 5. Set env vars (placeholders)
[Environment]::SetEnvironmentVariable("PEXELS_API_KEY", "{env:PEXELS_API_KEY}", "User")
[Environment]::SetEnvironmentVariable("GITHUB_PERSONAL_ACCESS_TOKEN", "{env:GITHUB_PERSONAL_ACCESS_TOKEN}", "User")
Write-Host "Env vars set (placeholders)."

# 6. Install deps (manual)
Write-Host "Please install: Python 3.12, Node.js, Bun, uv, ffmpeg, scrcpy, Docker"
Write-Host "Run download_deps.ps1 for direct links."

Write-Host "=== Installation complete ===" -ForegroundColor Green
Write-Host "Restart OpenCode to load agents/skills/MCPs."
pause
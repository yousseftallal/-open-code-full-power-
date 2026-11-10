# Direct download links for dependencies
$dest = "$PSScriptRoot\deps"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$links = @{
  "python312.exe" = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe"
  "node.msi" = "https://nodejs.org/dist/v24.16.0/node-v24.16.0-x64.msi"
  "bun.zip" = "https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip"
  "uv.zip" = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
  "ffmpeg.zip" = "https://github.com/GyanD/codexffmpeg/releases/download/9.0.2/ffmpeg-9.0.2-full_build.zip"
  "scrcpy.zip" = "https://github.com/Genymobile/scrcpy/releases/download/v5.0.1/scrcpy-win64-v5.0.1.zip"
  "docker.exe" = "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"
}

foreach ($name in $links.Keys) {
    $url = $links[$name]
    $out = Join-Path $dest $name
    Write-Host "Downloading $name ..."
    Invoke-WebRequest -Uri $url -OutFile $out
}
Write-Host "Done. Files saved to $dest"
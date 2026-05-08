param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"

& $Python -m pip install -r requirements.txt
& $Python -m pip install -r requirements-dev.txt
& $Python -c "import tkinter; root = tkinter.Tk(); root.destroy(); print('Tkinter OK')"
& $Python -m PyInstaller ytd_gui.spec --clean --noconfirm

Write-Host ""
Write-Host "Build complete: dist\YT Downloader\YT Downloader.exe"

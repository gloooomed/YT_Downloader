# Build with:
#   pyinstaller ytd_gui.spec
#
# Optional bundled FFmpeg:
#   Put ffmpeg.exe and ffprobe.exe in vendor/ffmpeg/bin before building.

from pathlib import Path


ROOT = Path(SPECPATH)
ffmpeg_binaries = []
for name in ("ffmpeg.exe", "ffprobe.exe"):
    binary = ROOT / "vendor" / "ffmpeg" / "bin" / name
    if binary.exists():
        ffmpeg_binaries.append((str(binary), "ffmpeg"))

ffmpeg_datas = []
for name in ("LICENSE", "README.txt"):
    data = ROOT / "vendor" / "ffmpeg" / name
    if data.exists():
        ffmpeg_datas.append((str(data), "ffmpeg"))


a = Analysis(
    ["run_gui.py"],
    pathex=[str(ROOT / "src")],
    binaries=ffmpeg_binaries,
    datas=ffmpeg_datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="YT Downloader",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="YT Downloader",
)

# YT Downloader

Windows-friendly YouTube downloader with a desktop GUI and a terminal CLI.

## Windows Release

Download the latest Windows release from:

[GitHub Releases](https://github.com/gloooomed/YT_Downloader/releases)

After downloading, extract the release zip and open the app by double-clicking:

```text
YT Downloader/YT Downloader.exe
```

Keep the full `YT Downloader` folder together when moving or sharing the app. The `_internal` folder contains the bundled Python runtime, packages, Tkinter files, and FFmpeg.

The Windows release includes FFmpeg, so video merging and audio conversion work without installing FFmpeg separately.

## GUI

```bash
python run_gui.py
```

The GUI lets you paste a YouTube URL, choose video or audio, pick quality/format, select an output folder, and start the download from a desktop window.

## CLI

```bash
python run.py
```

Downloads are saved to your system Downloads folder by default.

## Install From Source

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install the package locally:

```bash
python -m pip install -e .
```

CLI command:

```bash
ytd
```

GUI command:

```bash
ytd-gui
```

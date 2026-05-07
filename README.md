# YouTube Terminal Downloader

Interactive Python CLI for downloading YouTube videos or audio by pasting a link.

## Install

```bash
python -m pip install -r requirements.txt
```

Optional, for MP3 conversion:

Install FFmpeg from <https://ffmpeg.org/download.html> and make sure `ffmpeg` is available in your terminal.

## Run

```bash
python run.py
```

You can also run it as a module:

```bash
python -m pip install -e .
python -m yt_downloader
```

After installing the package locally, this command is available:

```bash
ytd
```

Downloads are saved to your system Downloads folder by default.

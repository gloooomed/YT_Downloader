from pathlib import Path
from shutil import which


class DownloaderError(RuntimeError):
    pass


def require_ytdlp():
    try:
        import yt_dlp
    except ImportError as exc:
        raise DownloaderError(
            "yt-dlp is not installed. Run: python -m pip install -r requirements.txt"
        ) from exc
    return yt_dlp


def build_options(media_type: str, quality: str, audio_format: str, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_available = has_ffmpeg()
    options = {
        "outtmpl": str(output_dir / "%(title).180s [%(id)s].%(ext)s"),
        "noplaylist": True,
        "restrictfilenames": False,
        "quiet": False,
        "no_warnings": False,
        "progress_hooks": [_progress],
    }

    if media_type == "audio":
        options["format"] = "bestaudio/best"
        if audio_format != "original" and ffmpeg_available:
            options["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": audio_format,
                    "preferredquality": "192",
                }
            ]
        return options

    if not ffmpeg_available:
        options["format"] = "best[ext=mp4]/best"
        return options

    if quality == "best":
        options["format"] = "bv*+ba/best"
    elif quality == "small":
        options["format"] = "worstvideo*+worstaudio/worst"
    else:
        options["format"] = f"bv*[height<={quality}]+ba/b[height<={quality}]/best"

    options["merge_output_format"] = "mp4"
    return options


def download(url: str, media_type: str, quality: str, audio_format: str, output_dir: Path) -> None:
    yt_dlp = require_ytdlp()
    options = build_options(media_type, quality, audio_format, output_dir)
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception as exc:
        raise DownloaderError(str(exc)) from exc


def _progress(status: dict) -> None:
    if status.get("status") == "finished":
        print("Processing downloaded file...")


def has_ffmpeg() -> bool:
    return which("ffmpeg") is not None and which("ffprobe") is not None

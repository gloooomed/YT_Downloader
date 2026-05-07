from .downloader import DownloaderError, download
from .paths import default_download_dir, resolve_output_dir
from .prompts import DownloadRequest, ask_choice, ask_required, ask_text


VIDEO_QUALITIES = {
    "1": "best",
    "2": "1080",
    "3": "720",
    "4": "480",
    "5": "small",
}

AUDIO_FORMATS = {
    "1": "original",
    "2": "mp3",
    "3": "m4a",
    "4": "opus",
}


def main() -> None:
    print("YouTube Terminal Downloader")
    print("Paste a YouTube link and choose video or audio.\n")

    while True:
        request = collect_request()
        try:
            print(f"\nSaving to: {request.output_dir}")
            download(
                request.url,
                request.media_type,
                request.quality,
                request.audio_format,
                request.output_dir,
            )
            print("\nFile downloaded.")
        except DownloaderError as exc:
            print(f"\nDownload failed: {exc}")

        again = ask_choice("\nWanna download another one", {"y": "yes", "n": "no"}, "n")
        if again == "n":
            break


def collect_request() -> DownloadRequest:
    url = ask_required("YouTube URL: ")
    media_type = ask_choice("Download type", {"v": "video", "a": "audio"}, "v")

    quality = "best"
    audio_format = "original"

    if media_type == "v":
        quality = ask_choice("Video quality", VIDEO_QUALITIES, "1")
        quality = VIDEO_QUALITIES[quality]
    else:
        audio_format = ask_choice("Audio format", AUDIO_FORMATS, "1")
        audio_format = AUDIO_FORMATS[audio_format]

    default_dir = str(default_download_dir())
    output_dir = resolve_output_dir(ask_text("Output folder", default_dir))

    return DownloadRequest(
        url=url,
        media_type="video" if media_type == "v" else "audio",
        quality=quality,
        audio_format=audio_format,
        output_dir=output_dir,
    )


if __name__ == "__main__":
    main()

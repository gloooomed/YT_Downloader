from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DownloadRequest:
    url: str
    media_type: str
    quality: str
    audio_format: str
    output_dir: Path


def ask_required(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def ask_choice(prompt: str, choices: dict[str, str], default: str) -> str:
    labels = " / ".join(
        f"{key}={name}" + (" default" if key == default else "")
        for key, name in choices.items()
    )
    while True:
        value = input(f"{prompt} ({labels}): ").strip().lower() or default
        if value in choices:
            return value
        print("Choose one of: " + ", ".join(choices))


def ask_text(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default

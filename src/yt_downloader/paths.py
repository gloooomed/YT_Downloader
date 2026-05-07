from pathlib import Path


def default_download_dir() -> Path:
    downloads = Path.home() / "Downloads"
    if downloads.exists():
        return downloads / "YouTube"
    return Path.cwd() / "downloads"


def resolve_output_dir(value: str) -> Path:
    if not value.strip():
        return default_download_dir()
    return Path(value).expanduser().resolve()

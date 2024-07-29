"""Utility module to manage meta info."""
import platform

from rich.console import Console

from . import __copyright__, __license__, __version__,__author__,__repository_url__,__original_repository_url__,__original_author__,__original_version__

APP_VERSION = f"Telegram Media Downloader {__version__}"
DEVICE_MODEL = f"{platform.python_implementation()} {platform.python_version()}"
SYSTEM_VERSION = f"{platform.system()} {platform.release()}"
LANG_CODE = "en"


def print_meta(logger):
    """Prints meta-data of the downloader script."""
    console = Console()
    # Print project information
    console.log(
        f"[bold]Telegram Media Downloader v{__version__} by {__author__}[/bold]\n"
        f"[i]Copyright (C) 2024 {__author__}[/i]"
    )
    console.log(f"Licensed under the terms of the {__license__}")
    console.log(f"Repository URL: {__repository_url__}")
    console.log(
        f"Based on Dineshkarthik's version {__original_version__} at {__original_repository_url__}"
    )
    # Print device and system information
    logger.info(f"Device: {DEVICE_MODEL} - {APP_VERSION}")
    logger.info(f"System: {SYSTEM_VERSION} ({LANG_CODE.upper()})")

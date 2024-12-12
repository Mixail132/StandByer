""" Making the relative paths to the project files."""

from pathlib import Path

DIR_ROOT = Path(__file__).parent.parent.resolve()
DIR_APP = DIR_ROOT / "app"
DIR_TEMP = DIR_ROOT / ".temp"
DIR_IMG = DIR_ROOT / "img"
DIR_OUT = DIR_ROOT / "out"

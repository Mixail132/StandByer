""" Making the relative paths to the project files."""

from pathlib import Path

DIR_ROOT = Path(__file__).parent.parent.resolve()

DIR_APP = DIR_ROOT / "app"
DIR_IMG = DIR_ROOT / "img"
DIR_LINT = DIR_ROOT / ".github" / "settings"
DIR_OUT = DIR_ROOT / "out"
DIR_TEMP = DIR_ROOT / ".temp"

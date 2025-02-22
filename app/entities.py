from dataclasses import dataclass
from app.dirs import DIR_IMG
from pathlib import Path


@dataclass
class Device:
    on: str
    off: str
    timing: bool = False
    clock: Path = DIR_IMG / "noclock.png"
    description: str = ""
    schedule: str = ""
    id: int | None = None
    ip: str = ""
    mark: Path = DIR_IMG / "grey.png"
    name: str = ""
    place: str = ""
    standby: str | None = None
    state: int = -1
    type: str = ""
    zone: str = ""


@dataclass
class Description:
    auto: str
    command: str
    description: str
    ip: str
    name: str
    on: str
    out: str
    place: str
    progress: str
    set: str
    standby: str
    state: str
    type: str
    zone: str


@dataclass
class Mode:
    debug: bool
    delay: int
    survey: int


@dataclass
class Mistakes:
    ip_bad: str
    time_off: str
    time_small: str
    time_equal: str

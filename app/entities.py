from dataclasses import dataclass


@dataclass
class Device:
    on: str
    off: str
    timing: bool = False
    clock: str | None = None
    description: str = ""
    id: int | None = None
    ip: str = ""
    mark: str = "../img/grey.png"
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

from dataclasses import dataclass


@dataclass
class Device:
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
    description: str
    ip: str
    name: str
    on: str
    out: str
    place: str
    standby: str
    state: str
    type: str
    zone: str

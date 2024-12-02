from dataclasses import dataclass


@dataclass
class DeviceConfig:
    ip: str
    place: str
    type: str
    zone: str
    description: str = ""
    mark: str = "../img/grey.png"
    standby: str | None = None
    state: int = -1


@dataclass
class CommonTitles:
    description: str
    header: str
    ip: str
    name: str
    place: str
    state: str
    type: str
    zone: str


from dataclasses import dataclass


@dataclass
class DeviceConfig:
    ip: str
    place: str
    type: str
    zone: str
    mark: str = "../img/grey.png"
    standby: str | None = None
    state: int = -1


@dataclass
class DeviceDescription:
    allocation: str
    header: str
    usage: str
    type: str
    state: str


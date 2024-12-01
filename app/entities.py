from dataclasses import dataclass


@dataclass
class AmplifierConfig:
    ip: str
    place: str
    type: str
    zone: str
    mark: str = "../img/grey.png"
    standby: str | None = None
    state: int = -1

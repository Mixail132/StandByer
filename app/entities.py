from dataclasses import dataclass


@dataclass
class AmplifierConfig:
    ip: str
    place: str
    type: str
    zone: str
    mark: str = "../img/grey.png"
    state: int = -1

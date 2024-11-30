from dataclasses import dataclass


@dataclass
class AmplifierConfig:
    ip: str
    zone: str
    type: str
    place: str
    state: int = -1

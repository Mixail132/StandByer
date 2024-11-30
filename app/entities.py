from dataclasses import dataclass


@dataclass
class AmplifierConfig:
    ip_address: str
    zone: str
    type: str
    place: str


@dataclass
class AmplifierState:
    standby: bool
    online: bool


@dataclass
class RequestPayload:
    check_state: str
    set_state: str

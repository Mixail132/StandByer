from dataclasses import dataclass
from environs import Env


@dataclass
class AmplifierConfig:
    ip_address: str = ""
    name: str = ""
    state: bool | None = None


def load_config() -> list:
    env: Env = Env()
    env.read_env(".env")
    amplifiers = []
    for i in range(1, 6):
        amplifier = AmplifierConfig(
            ip_address=env.str(f"A{i}_IP"),
            name=env.str(f"A{i}_NAME"),
        )
        amplifiers.append(amplifier)
    return amplifiers

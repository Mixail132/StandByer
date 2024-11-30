from entities import AmplifierConfig
from environs import Env

def read_config() -> list[AmplifierConfig]:
    """
    Reads the amplifiers' descriptions from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    amplifiers = []

    for num in range(1, 6):
        amplifier = AmplifierConfig(
            type=env.str(f"A{num}_TYPE"),
            ip=env.str(f"A{num}_IP"),
            zone=env.str(f"{num}_ZONE"),
            place=env.str(f"{num}_PLACE")
        )
        amplifiers.append(amplifier)

    return amplifiers

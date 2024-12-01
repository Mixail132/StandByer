from entities import DeviceConfig, DeviceDescription
from environs import Env


def read_config() -> list[DeviceConfig]:
    """
    Reads the devices' configs from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    devices = []

    for num in range(1, 6):
        device = DeviceConfig(
            type=env.str(f"A{num}_TYPE"),
            ip=env.str(f"A{num}_IP"),
            zone=env.str(f"A{num}_ZONE"),
            place=env.str(f"A{num}_PLACE")
        )
        devices.append(device)

    return devices


def read_description() -> DeviceDescription:
    """
    Reads the devices' descriptions from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    descriptions = DeviceDescription(
        allocation=env.str("ALLOCATION"),
        header=env.str("HEADER"),
        usage=env.str("USAGE"),
        type=env.str("TYPE"),
        state=env.str("STATE"),
    )

    return descriptions

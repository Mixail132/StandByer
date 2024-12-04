from entities import DeviceConfig, CommonTitles
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
            place=env.str(f"A{num}_PLACE"),
            name=env.str(f"A{num}_NAME"),
        )
        devices.append(device)

    return devices


def read_description() -> CommonTitles:
    """
    Reads the devices' descriptions from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    descriptions = CommonTitles(
        description=env.str("DESCRIPTION"),
        header=env.str("HEADER"),
        ip=env.str("IP"),
        name=env.str("NAME"),
        place=env.str("PLACE"),
        type=env.str("TYPE"),
        state=env.str("STATE"),
        zone=env.str("ZONE"),
        on=env.str("ON"),
        out=env.str("OUT"),
        standby=env.str("STANDBY"),
    )

    return descriptions

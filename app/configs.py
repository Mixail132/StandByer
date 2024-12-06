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
            ip=env.str(f"A{num}_IP"),
            name=env.str(f"A{num}_NAME"),
            place=env.str(f"A{num}_PLACE"),
            type=env.str(f"A{num}_TYPE"),
            zone=env.str(f"A{num}_ZONE"),
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
        ip=env.str("IP"),
        description=env.str("DESCRIPTION"),
        header=env.str("HEADER"),
        name=env.str("NAME"),
        on=env.str("ON"),
        out=env.str("OUT"),
        place=env.str("PLACE"),
        standby=env.str("STANDBY"),
        state=env.str("STATE"),
        type=env.str("TYPE"),
        zone=env.str("ZONE"),
    )

    return descriptions

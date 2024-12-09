from entities import Device, Description
from environs import Env


def read_config() -> list[Device]:
    """
    Reads the devices' configs from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    devices = []

    for num in range(1, 6):
        device = Device(
            id=num,
            ip=env.str(f"A{num}_IP"),
            name=env.str(f"A{num}_NAME"),
            place=env.str(f"A{num}_PLACE"),
            type=env.str(f"A{num}_TYPE"),
            zone=env.str(f"A{num}_ZONE"),
        )
        devices.append(device)

    return devices


def read_description() -> Description:
    """
    Reads the devices' descriptions from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    descriptions = Description(
        ip=env.str("IP"),
        description=env.str("DESCRIPTION"),
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


def save_config(devices: list[Device]) -> None:
    """
    Saves the given device parameters to the environment file.
    """
    var_file = ".env"
    file = open(var_file, "r")
    lines = file.readlines()
    output_lines = []
    for line in lines:

        output_line = line

        for device in devices:

            device_name = f"A{device.id}_NAME"
            device_place = f"A{device.id}_PLACE"
            device_zone = f"A{device.id}_ZONE"
            device_ip = f"A{device.id}_IP"
            device_type = f"A{device.id}_TYPE"

            if line.startswith(device_name):
                output_line = f"{device_name}={device.name}\n"
                continue
            elif line.startswith(device_place):
                output_line = f"{device_place}={device.place}\n"
                continue
            elif line.startswith(device_zone):
                output_line = f"{device_zone}={device.zone}\n"
                continue
            elif line.startswith(device_ip):
                output_line = f"{device_ip}={device.ip}\n"
                continue
            elif line.startswith(device_type):
                output_line = f"{device_type}={device.type}\n"
                continue

        output_lines.append(output_line)
    output_text = "".join(output_lines)

    file.close()

    file = open(var_file, "w")
    file.write(output_text)

    file.close()

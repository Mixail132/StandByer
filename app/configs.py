from entities import Debug, Device, Description
from environs import Env

env: Env = Env()
env.read_env()


def read_modes() -> Debug:
    """
    Read the program modes from the '.env' file.
    """
    debug = Debug(
        debug=env.bool("DEBUG")
    )
    return debug


def read_config() -> list[Device]:
    """
    Read the device configurations from the '.env' file.
    """
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
    Read the program descriptions from the '.env' file.
    """
    descriptions = Description(
        command=env.str("COMMAND"),
        ip=env.str("IP"),
        description=env.str("DESCRIPTION"),
        name=env.str("NAME"),
        on=env.str("ON"),
        out=env.str("OUT"),
        place=env.str("PLACE"),
        progress=env.str("PROGRESS"),
        set=env.str("SET"),
        standby=env.str("STANDBY"),
        state=env.str("STATE"),
        type=env.str("TYPE"),
        zone=env.str("ZONE"),
    )

    return descriptions


def save_config(devices: list[Device]) -> None:
    """
    Save the given device parameters to the '.env' file.
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

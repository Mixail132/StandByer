"""
A set of functions to read and save the devices' configuration.
The configured objects for import.
"""

from environs import Env

from app.entities import Description, Device, Mistakes, Mode

env: Env = Env()
env.read_env()


def read_program_modes() -> Mode:
    """
    Read the program modes from the '.env' file.
    """
    debug = Mode(
        debug=env.bool("DEBUG"),
        delay=env.int("DELAY"),
        survey=env.int("SURVEY"),
    )
    return debug

def read_mistake_messages() -> Mistakes:
    """
    Read the program mistake messages from the '.env' file.
    """
    mistake = Mistakes(
        ip_bad=env.str("IP_BAD"),
        time_equal=env.str("TIME_EQUAL"),
        time_off=env.str("TIME_OFF"),
        time_small=env.str("TIME_SMALL"),
    )
    return mistake


def read_devices_config() -> list[Device]:
    """
    Read the device configurations from the '.env' file.
    """
    devices = []

    for num in range(1, 7):
        device = Device(
            id=num,
            ip=env.str(f"A{num}_IP"),
            name=env.str(f"A{num}_NAME"),
            on=env.str(f"A{num}_ON"),
            off=env.str(f"A{num}_OFF"),
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
        auto=env.str("AUTO"),
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


def save_devices_config(devices: list[Device]) -> None:
    """
    Save the given device parameters to the '.env' file.
    """
    var_file = ".env"
    with open(var_file, "r", encoding="UTF-8") as lines:
        output_lines = []
        for line in lines:

            output_line = line

            for device in devices:

                if line.startswith(f"A{device.id}_NAME"):
                    output_line = f"A{device.id}_NAME={device.name}\n"

                elif line.startswith(f"A{device.id}_PLACE"):
                    output_line = f"A{device.id}_PLACE={device.place}\n"

                elif line.startswith(f"A{device.id}_ZONE"):
                    output_line = f"A{device.id}_ZONE={device.zone}\n"

                elif line.startswith(f"A{device.id}_IP"):
                    output_line = f"A{device.id}_IP={device.ip}\n"

                elif line.startswith(f"A{device.id}_TYPE"):
                    output_line = f"A{device.id}_TYPE={device.type}\n"

                elif line.startswith(f"A{device.id}_ON"):
                    output_line = f"A{device.id}_ON={device.on}\n"

                elif line.startswith(f"A{device.id}_OFF"):
                    output_line = f"A{device.id}_OFF={device.off}\n"

            output_lines.append(output_line)
        output_text = "".join(output_lines)

    with open(var_file, "w", encoding="UTF-8") as file:
        file.write(output_text)


initial_devices: list[Device] = read_devices_config()
program_mode: Mode = read_program_modes()
program_headers: Description = read_description()
program_mistakes: Mistakes = read_mistake_messages()

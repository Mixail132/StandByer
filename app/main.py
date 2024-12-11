import tkinter as tk

from tkinter import ttk

from actions import (
    set_random_states,
    set_real_state,
    set_state_mark)
from tooltips import ToolTip, set_tooltip
from configs import (
    read_modes,
    read_config,
    read_description,
    Debug,
    Device,
    Description)
from settings import settings_window


main = tk.Tk()
main.title("Device switcher")
main.geometry("670x280")


progress_bars = {}
selected_values = {}
state_images = {}
state_labels = {}
tooltips = {}
on_buttons = {}
off_buttons = {}


# def set_mark(devices: list[Device]) -> list[Device]:
#     """
#     Change the color of a circle mark.
#     Change the device pop-up description.
#     Change the 'on' radiobutton state.
#     Change the 'off' radiobutton state.
#
#     """
#     for device in devices:
#
#         device_id = device.id
#
#         if device_id in state_labels:
#
#             new_mark = device.mark
#             new_image = tk.PhotoImage(file=new_mark)
#
#             state_labels[device_id].config(image=new_image)
#             state_images[device_id] = new_image
#
#             tooltips[device_id].text = device.description
#
#             var = tk.StringVar(value=device.standby)
#             selected_values[device_id] = var
#
#             on_buttons[device_id].config(variable=var)
#             off_buttons[device_id].config(variable=var)
#
#     return devices


def get_command(device: Device) -> None:
    """
    Get the radiobutton state and a command from `OK` button.
    Start the progress bar.
    Set the progress bar moving time.
    Wait until the progress bar ends and call the command function.
    Deny the commands if the device is unreached (standby is None)
    :param device: the device configuration object.
    """
    device_id: int = device.id
    selected_value: str | None = selected_values[device_id].get()
    if device.standby and device.standby != selected_value:
        progress_bars[device_id].start()
        main.after(6220, lambda: launch_command(device, selected_value))


def launch_command(device: Device, selected_value: str) -> None:
    """
    Stop the progress bar.
    Send the given command to a device.
    Update a color circle mark according to a new device state.
    :param device: the device configuration object.
    :param selected_value: the value to be set in the command.
    """

    device_ip = device.ip
    standby_modes = {"on": False, "off": True}
    standby_mode = standby_modes[selected_value]

    if not program_mode.debug:
        command_result = set_real_state(device_ip, standby_mode)
        command_results = {"Active": 0, "Standby": 1, "Unreached": -1}
        device.state = command_results[command_result]

    elif program_mode.debug:
        all_states = {"on": 0, "off": 1, "out": None}
        device.state = all_states[selected_value]

    device_id: int = device.id
    progress_bars[device_id].stop()
    change_state(device)


def change_state(device: Device) -> None:
    """
    Change the color of the circle mark when sending
    a command to change the device's state.
    Change the pop-up description text when sending
    a command to change the device's state.
    Change the radio buttons' state.
    """
    device = set_state_mark(device)
    device_id: int = device.id

    new_mark = device.mark
    new_image = tk.PhotoImage(file=new_mark)

    state_labels[device_id].config(image=new_image)
    state_images[device_id] = new_image

    set_tooltip([device], program_headers)
    tooltips[device_id].text = device.description

    var = tk.StringVar(value=device.standby)
    selected_values[device_id] = var
    on_buttons[device_id].config(variable=var)
    off_buttons[device_id].config(variable=var)


def main_window(devices) -> None:
    """
    Create the main window and it's widgets.
    """
    name_header = ttk.Label(main, text=program_headers.state)
    name_header.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    type_header = ttk.Label(main, text=program_headers.type)
    type_header.grid(row=0, column=2, padx=5, pady=10, sticky="w")

    zone_header = ttk.Label(main, text=program_headers.zone)
    zone_header.grid(row=0, column=3, padx=30, pady=10, sticky="w")

    command_header = ttk.Label(main, text=program_headers.command)
    command_header.grid(row=0, column=4, columnspan=2, padx=5, pady=10, sticky="w")

    place_header = ttk.Label(main, text=program_headers.set)
    place_header.grid(row=0, column=6, padx=40, pady=10, sticky="w")

    progress_header = ttk.Label(main, text=program_headers.progress)
    progress_header.grid(row=0, column=7, padx=5, pady=10, sticky="w")

    for device in devices:

        id_label = ttk.Label(main, text=device.id)
        id_label.grid(row=device.id, column=0, padx=10, pady=5, sticky="w")

        state_image = tk.PhotoImage(file=device.mark)
        state_label = ttk.Label(main, image=state_image)

        state_label.image = state_image
        state_label.grid(row=device.id, column=1, padx=5, pady=5, sticky="w")

        state_labels[device.id] = state_label
        state_images[device.id] = state_image

        type_label = ttk.Label(main, text=device.type)
        type_label.grid(row=device.id, column=2, padx=5, pady=5, sticky="w")

        tooltip = ToolTip(type_label, device.description)
        tooltips[device.id] = tooltip

        zone_label = ttk.Label(main, text=device.zone)
        zone_label.grid(row=device.id, column=3, padx=30, pady=5, sticky="w")

        var = tk.StringVar(value=device.standby)
        selected_values[device.id] = var

        on_button = ttk.Radiobutton(main, text="on", value="on", variable=var)
        on_button.grid(row=device.id, column=4, padx=5, pady=5, sticky="w")
        on_buttons[device.id] = on_button

        off_button = ttk.Radiobutton(main, text="off", value="off", variable=var)
        off_button.grid(row=device.id, column=5, padx=5, pady=5, sticky="w")
        off_buttons[device.id] = off_button

        ok_button = ttk.Button(
            main,
            text="ok",
            command=lambda unit=device: get_command(unit)
        )
        ok_button.grid(row=device.id, column=6, padx=40, pady=5, sticky="w")

        progress_bar = ttk.Progressbar(main, orient="horizontal", length="106")
        progress_bar.grid(row=device.id, column=7, padx=5, pady=5, sticky="w")
        progress_bars[device.id] = progress_bar

    settings_button = ttk.Button(
        main,
        text="Settings",
        command=lambda: settings_window(main)
    )
    settings_button.grid(row=6, column=7, padx=35, pady=25, sticky="w")

    main.mainloop()


program_mode: Debug = read_modes()
device_initials: list[Device] = read_config()
device_states: list[Device] = set_random_states(device_initials)
program_headers: Description = read_description()
device_tooltips: list[Device] = set_tooltip(device_states, program_headers)
# device_marks = set_mark(device_tooltips)
main_window(device_tooltips)

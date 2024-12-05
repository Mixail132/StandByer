import tkinter as tk

from tkinter import ttk

from actions import get_mock_states, set_statemarks
from configs import (read_config,
                     read_description,
                     CommonTitles,
                     DeviceConfig)
from tooltips import ToolTip, get_tooltip

description: CommonTitles = read_description()

root = tk.Tk()


root.title(description.header)
root.geometry("750x240")

progress_bars = {}
selected_values = {}
state_images = {}
state_labels = {}
tooltips = {}


def update_states():
    dev_initials: list[DeviceConfig] = read_config()
    dev_states: list[DeviceConfig] = get_mock_states(dev_initials)
    _devices: list[DeviceConfig] = get_tooltip(dev_states)
    root.after(1000, update_states)
    return _devices


def get_command(unit: DeviceConfig) -> None:
    """
    Gets the radiobutton state and a command from `OK` button.
    :param unit: the device configuration object.
    """
    if unit.standby:
        unit_ip: str = unit.ip
        selected_value = selected_values[unit_ip].get()
        progress_bars[unit_ip].start()
        root.after(6220, lambda: send_command(unit, selected_value))


def send_command(unit: DeviceConfig, selected_value: str) -> None:
    """
    Sends the given command to a device.
    Updates a color circle mark according to a new state
    of the device.
    :param unit: the device configuration object.
    :param selected_value: the value to be set in the command.
    """
    all_states = {"on": 0, "off": 1, "out": None}
    unit_ip: str = unit.ip
    progress_bars[unit_ip].stop()

    if unit.standby != selected_value:
        unit.state = all_states[selected_value]
        change_state(unit)


def change_state(unit):

    set_statemarks(unit)
    unit_ip: str = unit.ip
    new_mark = unit.mark
    new_image = tk.PhotoImage(file=new_mark)
    state_labels[unit_ip].config(image=new_image)
    state_images[unit_ip] = new_image

    get_tooltip([unit])
    tooltips[unit_ip].text = unit.description


def main_window():
    devices = update_states()

    for num, device in enumerate(devices, 1):

        number_label = ttk.Label(root, text=num)
        number_label.grid(row=num, column=0, padx=5, pady=5, sticky="w")

        state_image = tk.PhotoImage(file=device.mark)
        state_label = ttk.Label(root, image=state_image)
        state_label.image = state_image
        state_label.grid(row=num, column=1, padx=5, pady=5, sticky="w")
        state_labels[device.ip] = state_label
        state_images[device.ip] = state_image

        type_label = ttk.Label(root, text=device.type)
        type_label.grid(row=num, column=2, padx=5, pady=5, sticky="w")
        tooltip = ToolTip(type_label, device.description)
        tooltips[device.ip] = tooltip

        zone_label = ttk.Label(root, text=device.zone)
        zone_label.grid(row=num, column=3, padx=30, pady=5, sticky="w")

        var = tk.StringVar(value=device.standby)
        selected_values[device.ip] = var
        on_button = ttk.Radiobutton(root, text="on", value="on", variable=var)
        on_button.grid(row=num, column=4, padx=5, pady=5, sticky="w")

        off_button = ttk.Radiobutton(root, text="off", value="off", variable=var)
        off_button.grid(row=num, column=5, padx=5, pady=5, sticky="w")

        ok_button = ttk.Button(
            root,
            text="ok",
            command=lambda unit=device: get_command(unit)
        )
        ok_button.grid(row=num, column=6, padx=40, pady=5, sticky="w")

        progress_bar = ttk.Progressbar(root, orient="horizontal", length="106")
        progress_bar.grid(row=num, column=7, padx=5, pady=5, sticky="w")
        progress_bars[device.ip] = progress_bar

    update_states()

    settings_button = ttk.Button(root, text="Settings")
    settings_button.grid(row=6, column=8, padx=35, pady=25, sticky="w")

    root.mainloop()


main_window()

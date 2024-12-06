import tkinter as tk

from tkinter import ttk

from actions import get_mock_states, set_statemarks
from configs import (read_config,
                     read_description,
                     CommonTitles,
                     DeviceConfig)
from tooltips import ToolTip, get_tooltip
from settings_window import settings_window

description: CommonTitles = read_description()

main = tk.Tk()
main.title(description.header)
main.geometry("640x240")


progress_bars = {}
selected_values = {}
state_images = {}
state_labels = {}
tooltips = {}


def update_states() -> list[DeviceConfig]:
    dev_initials: list[DeviceConfig] = read_config()
    dev_states: list[DeviceConfig] = get_mock_states(dev_initials)
    _devices: list[DeviceConfig] = get_tooltip(dev_states)
    main.after(1000, update_states)
    return _devices


def get_command(unit: DeviceConfig) -> None:
    """
    Gets the radiobutton state and a command from `OK` button.
    :param unit: the device configuration object.
    """
    if unit.standby:
        unit_id: int = unit.id
        selected_value = selected_values[unit_id].get()
        progress_bars[unit_id].start()
        main.after(6220, lambda: send_command(unit, selected_value))


def send_command(unit: DeviceConfig, selected_value: str) -> None:
    """
    Sends the given command to a device.
    Updates a color circle mark according to a new state
    of the device.
    :param unit: the device configuration object.
    :param selected_value: the value to be set in the command.
    """
    all_states = {"on": 0, "off": 1, "out": None}
    unit_id: int = unit.id
    progress_bars[unit_id].stop()

    if unit.standby != selected_value:
        unit.state = all_states[selected_value]
        change_state(unit)


def change_state(unit):

    set_statemarks(unit)
    unit_id: int = unit.id
    new_mark = unit.mark
    new_image = tk.PhotoImage(file=new_mark)
    state_labels[unit_id].config(image=new_image)
    state_images[unit_id] = new_image

    get_tooltip([unit])
    tooltips[unit_id].text = unit.description


def main_window():
    devices = update_states()

    for number, device in enumerate(devices, 1):

        number_label = ttk.Label(main, text=number)
        number_label.grid(row=number, column=0, padx=5, pady=5, sticky="w")

        state_image = tk.PhotoImage(file=device.mark)
        state_label = ttk.Label(main, image=state_image)
        state_label.image = state_image
        state_label.grid(row=number, column=1, padx=5, pady=5, sticky="w")
        state_labels[device.id] = state_label
        state_images[device.id] = state_image

        type_label = ttk.Label(main, text=device.type)
        type_label.grid(row=number, column=2, padx=5, pady=5, sticky="w")
        tooltip = ToolTip(type_label, device.description)
        tooltips[device.id] = tooltip

        zone_label = ttk.Label(main, text=device.zone)
        zone_label.grid(row=number, column=3, padx=30, pady=5, sticky="w")

        var = tk.StringVar(value=device.standby)
        selected_values[device.id] = var
        on_button = ttk.Radiobutton(main, text="on", value="on", variable=var)
        on_button.grid(row=number, column=4, padx=5, pady=5, sticky="w")

        off_button = ttk.Radiobutton(main, text="off", value="off", variable=var)
        off_button.grid(row=number, column=5, padx=5, pady=5, sticky="w")

        ok_button = ttk.Button(
            main,
            text="ok",
            command=lambda unit=device: get_command(unit)
        )
        ok_button.grid(row=number, column=6, padx=40, pady=5, sticky="w")

        progress_bar = ttk.Progressbar(main, orient="horizontal", length="106")
        progress_bar.grid(row=number, column=7, padx=5, pady=5, sticky="w")
        progress_bars[device.id] = progress_bar

    update_states()

    settings_button = ttk.Button(
        main,
        text="Settings",
        command=lambda root=main: settings_window(root)
    )
    settings_button.grid(row=6, column=7, padx=35, pady=25, sticky="w")

    main.mainloop()


main_window()

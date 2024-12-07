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
    """
    Get initial devices descriptions.
    Get the devices' fake states.
    Get the devices' pop-up descriptions.
    Update the devices' states periodically.
    Return the list of devices' objects.
    """
    dev_initials: list[DeviceConfig] = read_config()
    dev_states: list[DeviceConfig] = get_mock_states(dev_initials)
    _devices: list[DeviceConfig] = get_tooltip(dev_states)

    for device in _devices:
        unit_id = device.id
        if unit_id in state_labels:
            new_mark = device.mark
            new_image = tk.PhotoImage(file=new_mark)
            state_labels[unit_id].config(image=new_image)
            state_images[unit_id] = new_image
            tooltips[unit_id].text = device.description

    main.after(5000, update_states)
    return _devices


def get_command(unit: DeviceConfig) -> None:
    """
    Gets the radiobutton state and a command from `OK` button.
    :param unit: the device configuration object.
    """
    if unit.standby:
        unit_id: int = unit.id
        selected_value: str | None = selected_values[unit_id].get()
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


def change_state(unit) -> None:
    """
    Changes the color of the circle mark when sending a command
    to change the device's state.
    Change a pop-up description text when sending a command
    to change the device's state.
    """
    set_statemarks(unit)
    unit_id: int = unit.id
    new_mark = unit.mark
    new_image = tk.PhotoImage(file=new_mark)
    state_labels[unit_id].config(image=new_image)
    state_images[unit_id] = new_image

    get_tooltip([unit])
    tooltips[unit_id].text = unit.description


def main_window() -> None:
    """
    Creates a main window and it's widgets.
    """
    devices = update_states()

    for device in devices:

        id_label = ttk.Label(main, text=device.id)
        id_label.grid(row=device.id, column=0, padx=5, pady=5, sticky="w")

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

        off_button = ttk.Radiobutton(main, text="off", value="off", variable=var)
        off_button.grid(row=device.id, column=5, padx=5, pady=5, sticky="w")

        ok_button = ttk.Button(
            main,
            text="ok",
            command=lambda unit=device: get_command(unit)
        )
        ok_button.grid(row=device.id, column=6, padx=40, pady=5, sticky="w")

        progress_bar = ttk.Progressbar(main, orient="horizontal", length="106")
        progress_bar.grid(row=device.id, column=7, padx=5, pady=5, sticky="w")
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

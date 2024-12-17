import tkinter as tk

from tkinter import ttk

from app.actions import set_random_states, set_real_state
from app.actions import set_state_mark, set_clock_mark
from app.actions import check_devices_states
from app.tooltips import ToolTip, set_tooltip
from app.configs import Device
from app.configs import initial_devices, program_mode, program_headers
from app.settings import create_settings_window
from app.timings import create_timings_window
from app.dirs import DIR_IMG

main = tk.Tk()
main.title("Device switcher")
main.iconbitmap(DIR_IMG / "note.ico")
main.geometry("655x320")


progress_bars = {}
selected_values = {}
clock_labels = {}
clock_images = {}
state_images = {}
state_labels = {}
type_labels = {}
zone_labels = {}
tooltips = {}
on_buttons = {}
off_buttons = {}


def update_devices_timings(devices: list[Device]) -> None:
    """
    Update the devices' clock marks if the schedule is set.
    """
    for device in devices:
        set_clock_mark(device)
        change_device_state(device)

    after_id = main.after(1000, lambda: update_devices_timings(devices))
    main.after_cancel(after_id)


def update_devices_states(devices: list[Device]) -> None:
    """
    Update the devices' state periodically.
    """
    if not program_mode.debug:
        devices = check_devices_states(devices)

    else:
        devices = set_random_states(devices)

    for device in devices:
        change_device_state(device)

    survey = program_mode.survey
    main.after(survey, lambda: update_devices_states(devices))


def get_button_command(device: Device) -> None:
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
        main.after(6220, lambda: launch_button_command(device, selected_value))


def launch_button_command(device: Device, selected_value: str) -> None:
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
    change_device_state(device)


def change_device_state(device: Device) -> None:
    """
    Change the color of the circle mark when sending
    a command to change the device's state.
    Change the pop-up description text when sending
    a command to change the device's state.
    Change the radio buttons' state.
    """
    device = set_state_mark(device)
    device = set_clock_mark(device)

    device_id: int = device.id

    new_state_mark = device.mark
    new_state_image = tk.PhotoImage(file=new_state_mark)

    state_labels[device_id].config(image=new_state_image)
    state_images[device_id] = new_state_image

    new_clock_mark = device.clock
    new_clock_image = tk.PhotoImage(file=new_clock_mark)

    clock_labels[device_id].config(image=new_clock_image)
    clock_images[device_id] = new_clock_image

    type_labels[device_id].config(text=device.type)
    zone_labels[device_id].config(text=device.zone)

    set_tooltip([device], program_headers)
    tooltips[device_id].text = device.description

    var = tk.StringVar(value=device.standby)
    selected_values[device_id] = var

    on_buttons[device_id].config(variable=var)
    off_buttons[device_id].config(variable=var)


def create_main_window(devices) -> None:
    """
    Create the main window and it's widgets.
    """
    state_header = ttk.Label(main, text=program_headers.state)
    state_header.grid(row=0, column=1, pady=10, sticky="w")

    type_header = ttk.Label(
        main,
        text=program_headers.type,
        width=12,
        anchor="center"
    )
    type_header.grid(row=0, column=2, pady=10, sticky="w")

    zone_header = ttk.Label(
        main,
        text=program_headers.zone,
        width=20,
        anchor="center"
    )
    zone_header.grid(row=0, column=3, pady=10, sticky="w")

    command_header = ttk.Label(
        main,
        text=program_headers.command,
        width=16,
        anchor="center"
    )
    command_header.grid(row=0, column=4, columnspan=2, pady=10, sticky="w")

    auto_header = ttk.Label(
        main,
        text=program_headers.auto,
        width=7,
        anchor="center"
    )
    auto_header.grid(row=0, column=6, pady=10, sticky="w")

    set_header = ttk.Label(
        main,
        text=program_headers.set,
        width=13,
        anchor="center"
    )
    set_header.grid(row=0, column=7, pady=10, sticky="w")

    progress_header = ttk.Label(
        main,
        text=program_headers.progress,
        width=20,
        anchor="center"
    )
    progress_header.grid(row=0, column=8, pady=10, sticky="w")

    for device in devices:

        id_label = ttk.Label(main, text=device.id)
        id_label.grid(row=device.id, column=0, padx=10, pady=5, sticky="w")

        state_image = tk.PhotoImage(file=device.mark)
        state_label = ttk.Label(main, image=state_image)

        state_label.image = state_image
        state_label.grid(row=device.id, column=1, padx=5, pady=5, sticky="w")

        state_labels[device.id] = state_label
        state_images[device.id] = state_image

        type_label = ttk.Label(main, text=device.type, width=12)
        type_labels[device.id] = type_label
        type_label.grid(row=device.id, column=2, padx=5, pady=5, sticky="w")

        tooltip = ToolTip(type_label, device.description)
        tooltips[device.id] = tooltip

        zone_label = ttk.Label(main, text=device.zone, width=20)
        zone_labels[device.id] = zone_label
        zone_label.grid(row=device.id, column=3, padx=5, pady=5, sticky="w")

        var = tk.StringVar(value=device.standby)
        selected_values[device.id] = var

        on_button = ttk.Radiobutton(main, text="on", value="on", variable=var)
        on_button.grid(row=device.id, column=4, padx=5, pady=5, sticky="w")
        on_buttons[device.id] = on_button

        off_button = ttk.Radiobutton(main, text="off", value="off", variable=var)
        off_button.grid(row=device.id, column=5, padx=7, pady=5, sticky="w")
        off_buttons[device.id] = off_button

        clock_image = tk.PhotoImage(file=device.clock)
        clock_label = ttk.Label(main, image=clock_image)
        clock_label.image = clock_image
        clock_label.grid(row=device.id, column=6, padx=10, pady=5, sticky="w")

        clock_labels[device.id] = clock_label
        clock_images[device.id] = clock_image

        ok_button = ttk.Button(
            main,
            text="ok",
            command=lambda unit=device: get_button_command(unit)
        )
        ok_button.grid(row=device.id, column=7, padx=5, pady=5, sticky="w")

        progress_bar = ttk.Progressbar(main, orient="horizontal", length="106")
        progress_bar.grid(row=device.id, column=8, padx=5, pady=5, sticky="w")
        progress_bars[device.id] = progress_bar

    auto_button = ttk.Button(
        main,
        text="Auto",
        command=lambda: create_timings_window(main, devices, update_devices_timings)
    )
    auto_button.grid(row=7, column=7, padx=5, pady=25, sticky="w")

    settings_button = ttk.Button(
        main,
        text="Settings",
        command=lambda: create_settings_window(main, devices, update_devices_states)
    )
    settings_button.grid(row=7, column=8, padx=10, pady=25, sticky="w")

    delay = program_mode.delay
    main.after(delay, lambda units=devices: update_devices_states(units))

    main.mainloop()


initial_devices: list[Device] = set_tooltip(initial_devices, program_headers)

for item in initial_devices:
    set_clock_mark(item)


create_main_window(initial_devices)

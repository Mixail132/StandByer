import tkinter as tk
from tkinter import ttk
from actions import get_mock_state
from configs import read_description

devices = get_mock_state()
description = read_description()

root = tk.Tk()
root.title(description.header)
root.geometry("750x200")

selected_values = {}
progress_bars = {}


def get_command(dev_ip: str) -> None:
    """
    Gets the radiobutton state and a command from `OK` button.
    :param dev_ip: the device ip address.
    """
    selected_value = selected_values[dev_ip].get()
    progress_bars[dev_ip].start()
    root.after(6260, lambda: send_command(dev_ip, selected_value))


def send_command(dev_ip: str, selected_value: str) -> None:
    """
    Sends the given command to a device.
    :param dev_ip: the device ip address.
    :param selected_value: the value to be set in the command.
    """
    progress_bars[dev_ip].stop()
    print(f"{device.ip} set standby: {selected_value}")


for num, device in enumerate(devices, 1):

    number_label = ttk.Label(root, text=num)
    number_label.grid(row=num, column=0, padx=5, pady=5, sticky="w")

    state_image = tk.PhotoImage(file=device.mark)
    state_label = ttk.Label(root, image=state_image)
    state_label.image = state_image
    state_label.grid(row=num, column=1, padx=5, pady=5, sticky="w")

    type_label = ttk.Label(root, text=device.type)
    type_label.grid(row=num, column=2, padx=5, pady=5, sticky="w")

    zone_label = ttk.Label(root, text=device.zone)
    zone_label.grid(row=num, column=3, padx=30, pady=5, sticky="w")

    var = tk.StringVar(value=device.standby)
    selected_values[device.ip] = var
    on_button = ttk.Radiobutton(root, text="on", value="on", variable=var)
    on_button.grid(row=num, column=4, padx=5, pady=5, sticky="w")

    off_button = ttk.Radiobutton(root, text="off", value="off", variable=var)
    off_button.grid(row=num, column=5, padx=5, pady=5, sticky="w")

    ok_button = ttk.Button(root, text="ok", command=lambda ip=device.ip: get_command(ip))
    ok_button.grid(row=num, column=6, padx=40, pady=5, sticky="w")

    progress_bar = ttk.Progressbar(root, orient="horizontal", length="100")
    progress_bar.grid(row=num, column=7, padx=5, pady=5, sticky="w")
    progress_bars[device.ip] = progress_bar

root.mainloop()

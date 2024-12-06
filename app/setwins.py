import ipaddress
import tkinter as tk
from tkinter import ttk
from entities import CommonTitles, DeviceConfig
from configs import read_description
from configs import read_config


devices: list[DeviceConfig] = read_config()
description: CommonTitles = read_description()

def settings_window(root):

    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.geometry("800x320")

    name_label = ttk.Label(settings, text=description.name)
    name_label.grid(row=1, column=1, padx=5, pady=10, sticky="w")

    type_label = ttk.Label(settings, text=description.type)
    type_label.grid(row=1, column=2, padx=5, pady=10, sticky="w")

    zone_label = ttk.Label(settings, text=description.zone)
    zone_label.grid(row=1, column=3, padx=5, pady=10, sticky="w")

    ip_label = ttk.Label(settings, text=description.ip)
    ip_label.grid(row=1, column=4, padx=5, pady=10, sticky="w")

    place_label = ttk.Label(settings, text=description.place)
    place_label.grid(row=1, column=5, padx=5, pady=10, sticky="w")

    for number, device in enumerate(devices, 2):

        number_label = ttk.Label(settings, text=number-1)
        number_label.grid(row=number, column=0, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings, width=28)
        name_label.insert(0, device.name)
        name_label.grid(row=number, column=1, padx=5, pady=10, sticky="w")

        type_label = ttk.Entry(settings, width=15)
        type_label.insert(0, device.type)
        type_label.grid(row=number, column=2, padx=5, pady=10, sticky="w")

        zone_label = ttk.Entry(settings, width=20)
        zone_label.insert(0, device.zone)
        zone_label.grid(row=number, column=3, padx=5, pady=10, sticky="w")

        ip_label = ttk.Entry(settings, width=15)
        ip_label.insert(0, device.ip)
        ip_label.grid(row=number, column=4, padx=5, pady=10, sticky="w")

        place_label = ttk.Entry(settings, width=12)
        place_label.insert(0, device.place)
        place_label.grid(row=number, column=5, padx=5, pady=10, sticky="w")

    apply_button = ttk.Button(settings, text="Apply")
    apply_button.grid(row=7, column=6, padx=10, pady=25, sticky="w")

    settings.mainloop()


def validate_ip(host):

    try:
        is_valid = ipaddress.ip_address(host)
        ip_is_valid = bool(is_valid)
    except ValueError:
        ip_is_valid = False

    return ip_is_valid

import ipaddress
import tkinter as tk
from tkinter import ttk

from entities import CommonTitles
from entities import DeviceConfig

from configs import read_description
from configs import read_config
from configs import save_config


devices: list[DeviceConfig] = read_config()
description: CommonTitles = read_description()

device_ips = {}
device_names = {}
device_types = {}
device_places = {}
device_zones = {}


def settings_window(root):

    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.geometry("680x320")

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

    for device in devices:

        id_label = ttk.Label(settings, text=device.id)
        id_label.grid(row=device.id, column=0, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings, width=28)
        name_label.insert(0, device.name)
        name_label.grid(row=device.id, column=1, padx=5, pady=10, sticky="w")
        device_names[device.id] = name_label

        type_label = ttk.Entry(settings, width=15)
        type_label.insert(0, device.type)
        type_label.grid(row=device.id, column=2, padx=5, pady=10, sticky="w")
        device_types[device.id] = type_label

        zone_label = ttk.Entry(settings, width=20)
        zone_label.insert(0, device.zone)
        zone_label.grid(row=device.id, column=3, padx=5, pady=10, sticky="w")
        device_zones[device.id] = zone_label

        ip_label = ttk.Entry(settings, width=15)
        ip_label.insert(0, device.ip)
        ip_label.grid(row=device.id, column=4, padx=5, pady=10, sticky="w")
        device_ips[device.id] = ip_label

        place_label = ttk.Entry(settings, width=14)
        place_label.insert(0, device.place)
        place_label.grid(row=device.id, column=5, padx=5, pady=10, sticky="w")
        device_places[device.id] = place_label

    apply_button = ttk.Button(
        settings,
        text="Save",
        command=save_settings,
    )
    apply_button.grid(row=7, column=5, padx=10, pady=25, sticky="w")

    settings.mainloop()


def save_settings():
    """
    Gets the settings from the form,
    Calls the function to save the settings to the ".env" file.
    """

    for device in devices:

        device.name = device_names[device.id].get()
        device.type = device_types[device.id].get()
        device.zone = device_zones[device.id].get()
        device_ip = device_ips[device.id].get()
        device.place = device_places[device.id].get()

        ip_is_valid = validate_ip(device_ip)
        if ip_is_valid:
            device.ip = device_ip

    save_config(devices)


def validate_ip(host):

    try:
        is_valid = ipaddress.ip_address(host)
        ip_is_valid = bool(is_valid)
    except ValueError:
        ip_is_valid = False

    return ip_is_valid

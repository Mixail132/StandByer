import ipaddress
import tkinter as tk
from tkinter import ttk
from entities import CommonTitles, DeviceConfig
from configs import read_description
from configs import read_config


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
        new_name = name_label.get()
        device_names[device.id] = new_name

        type_label = ttk.Entry(settings, width=15)
        type_label.insert(0, device.type)
        type_label.grid(row=device.id, column=2, padx=5, pady=10, sticky="w")
        new_type = type_label.get()
        device_types[device.id] = new_type

        zone_label = ttk.Entry(settings, width=20)
        zone_label.insert(0, device.zone)
        zone_label.grid(row=device.id, column=3, padx=5, pady=10, sticky="w")
        new_zone = zone_label.get()
        device_zones[device.id] = new_zone

        ip_label = ttk.Entry(settings, width=15)
        ip_label.insert(0, device.ip)
        ip_label.grid(row=device.id, column=4, padx=5, pady=10, sticky="w")
        new_ip = ip_label.get()
        device_ips[device.id] = new_ip

        place_label = ttk.Entry(settings, width=14)
        place_label.insert(0, device.place)
        place_label.grid(row=device.id, column=5, padx=5, pady=10, sticky="w")
        new_place=place_label.get()
        device_places[device.id] = new_place

    apply_button = ttk.Button(
        settings,
        text="Save",
    )
    apply_button.grid(row=7, column=5, padx=10, pady=25, sticky="w")

    settings.mainloop()


def validate_ip(host):

    try:
        is_valid = ipaddress.ip_address(host)
        ip_is_valid = bool(is_valid)
    except ValueError:
        ip_is_valid = False

    return ip_is_valid

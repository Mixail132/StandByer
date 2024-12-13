import ipaddress
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.configs import save_config
from app.configs import initial_devices, program_headers
from app.dirs import DIR_IMG


device_ips = {}
device_names = {}
device_types = {}
device_places = {}
device_zones = {}


def settings_window(root) -> None:
    """
    Create the settings window with its widgets.
    """
    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.iconbitmap(DIR_IMG / "note.ico")
    settings.geometry("680x300")

    name_header = ttk.Label(settings, text=program_headers.name)
    name_header.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    type_header = ttk.Label(settings, text=program_headers.type)
    type_header.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    zone_header = ttk.Label(settings, text=program_headers.zone)
    zone_header.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    ip_header = ttk.Label(settings, text=program_headers.ip)
    ip_header.grid(row=0, column=4, padx=5, pady=5, sticky="w")

    place_header = ttk.Label(settings, text=program_headers.place)
    place_header.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    for device in initial_devices:

        id_label = ttk.Label(settings, text=device.id)
        id_label.grid(row=device.id, column=0, padx=10, pady=10, sticky="w")

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
        command=lambda: save_settings(settings),
    )
    apply_button.grid(row=7, column=5, padx=10, pady=25, sticky="w")

    settings.mainloop()


def save_settings(settings: tk.Toplevel) -> None:
    """
    Get the settings from the form,
    Redefines the Device objects attribute with given values.
    Call the function to save the settings to the ".env" file.
    """
    for device in initial_devices:

        device.name = device_names[device.id].get()
        device.type = device_types[device.id].get()
        device.zone = device_zones[device.id].get()
        device.ip = device_ips[device.id].get()
        device.place = device_places[device.id].get()

    for device in initial_devices:
        ip_is_valid = validate_ip(device.ip)
        if not ip_is_valid:
            messagebox.showerror("Error", "Bad IP address!")
            break
    else:
        save_config(initial_devices)
        settings.destroy()


def validate_ip(host: str) -> bool:
    """
    Check whether the given ip address is valid.
    """
    try:
        is_valid = ipaddress.ip_address(host)
        ip_is_valid = bool(is_valid)

    except ValueError:
        ip_is_valid = False

    return ip_is_valid

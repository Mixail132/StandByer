import ipaddress
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.configs import save_devices_config
from app.configs import program_headers, program_mistakes
from app.entities import Device
from app.dirs import DIR_IMG


device_ips = {}
device_names = {}
device_types = {}
device_places = {}
device_zones = {}


def create_settings_window(
        root: tk.Tk,
        devices: list[Device],
        callback: callable
) -> None:
    """
    Create the settings window with its widgets.
    """
    global settings
    if settings is None or not settings.winfo_exists():

        settings = tk.Toplevel(root)
        settings.title("Settings")
        settings.iconbitmap(DIR_IMG / "note.ico")
        settings.geometry("675x340")

        name_header = ttk.Label(
            settings,
            text=program_headers.name,
            width=26,
            anchor="center")
        name_header.grid(row=0, column=1, pady=5, sticky="w")

        type_header = ttk.Label(
            settings,
            text=program_headers.type,
            width=15,
            anchor="center"
        )
        type_header.grid(row=0, column=2, pady=5, sticky="w")

        zone_header = ttk.Label(
            settings,
            text=program_headers.zone,
            width=20,
            anchor="center"
        )
        zone_header.grid(row=0, column=3, pady=5, sticky="w")

        ip_header = ttk.Label(
            settings,
            text=program_headers.ip,
            width=13,
            anchor="center"
        )
        ip_header.grid(row=0, column=4, pady=5, sticky="w")

        place_header = ttk.Label(
            settings,
            text=program_headers.place,
            width=14,
            anchor="center"
        )
        place_header.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        for device in devices:

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

            ip_label = ttk.Entry(settings, width=14)
            ip_label.insert(0, device.ip)
            ip_label.grid(row=device.id, column=4, padx=5, pady=10, sticky="w")
            device_ips[device.id] = ip_label

            place_label = ttk.Entry(settings, width=14)
            place_label.insert(0, device.place)
            place_label.grid(row=device.id, column=5, padx=5, pady=10, sticky="w")
            device_places[device.id] = place_label

        cancel_button = ttk.Button(
            settings,
            text="Cancel",
            command=lambda: settings.destroy()
        )
        cancel_button.grid(row=7, column=4, padx=(18, 0), pady=25, sticky="w")

        save_button = ttk.Button(
            settings,
            text="Save",
            command=lambda: save_devices_settings(settings, devices, callback),
        )
        save_button.grid(row=7, column=5, padx=5, pady=25, sticky="w")

        settings.mainloop()
    else:
        settings.focus_force()


def save_devices_settings(
        _settings: tk.Toplevel,
        devices: list[Device],
        callback: callable
) -> None:
    """
    Get the settings from the form,
    Redefines the Device objects attribute with given values.
    Call the function to save the settings to the ".env" file.
    """
    for device in devices:

        device.name = device_names[device.id].get()
        device.type = device_types[device.id].get()
        device.zone = device_zones[device.id].get()
        device.ip = device_ips[device.id].get()
        device.place = device_places[device.id].get()

    for device in devices:
        ip_is_valid = validate_given_ip(device.ip)
        if not ip_is_valid:
            messagebox.showerror("Error", program_mistakes.ip_bad, parent=_settings)
            break
    else:
        save_devices_config(devices)
        _settings.destroy()

        callback(devices)


def validate_given_ip(ip_address: str) -> bool:
    """
    Check whether the given ip address is valid.
    """
    try:
        is_valid = ipaddress.ip_address(ip_address)
        ip_is_valid = bool(is_valid)

    except ValueError:
        ip_is_valid = False

    return ip_is_valid


settings = None

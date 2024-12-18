import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.configs import program_headers, save_devices_config
from app.entities import Device
from app.dirs import DIR_IMG


dropdown_on_values = {}
dropdown_off_values = {}
dropdown_on_menus = {}
dropdown_off_menus = {}


def create_time_list() -> list:
    """
    Create a list of drop down menu items.
    """
    hours = ["-- :--"]
    for hour in range(15, 24):
        if len(str(hour)) == 2:
            hours.append(f"{hour}:00")
            hours.append(f"{hour}:05")
            hours.append(f"{hour}:10")
            hours.append(f"{hour}:15")
            hours.append(f"{hour}:20")
            hours.append(f"{hour}:25")
            hours.append(f"{hour}:30")
            hours.append(f"{hour}:35")
            hours.append(f"{hour}:40")
            hours.append(f"{hour}:45")
            hours.append(f"{hour}:50")
            hours.append(f"{hour}:55")
        else:
            hours.append(f"0{hour}:00")
    return hours


def create_timings_window(
        root: tk.Tk,
        devices: list[Device],
        callback: callable,
) -> None:
    """
    Create the timings window with its widgets.
    """
    global timings
    if timings is None or not timings.winfo_exists():
        timings = tk.Toplevel(root)
        timings.title("Timings")
        timings.iconbitmap(DIR_IMG / "note.ico")
        timings.geometry("428x305")

        type_header = ttk.Label(
            timings,
            text=program_headers.type,
            width=12,
            anchor="center"
        )
        type_header.grid(row=0, column=2, pady=10, sticky="w")

        zone_header = ttk.Label(
            timings,
            text=program_headers.zone,
            width=20,
            anchor="center"
        )
        zone_header.grid(row=0, column=3, pady=10, sticky="w")

        on_header = ttk.Label(timings, text="On", width=10, anchor="center")
        on_header.grid(row=0, column=4, pady=10, sticky="w")

        off_header = ttk.Label(timings, text="Off", width=10, anchor="center")
        off_header.grid(row=0, column=5, pady=10, sticky="w")

        options = create_time_list()

        for device in devices:

            id_label = ttk.Label(timings, text=device.id)
            id_label.grid(row=device.id, column=0, padx=10, pady=5, sticky="w")

            type_label = ttk.Label(timings, text=device.type, width=12)
            type_label.grid(row=device.id, column=2, padx=5, pady=5, sticky="w")

            zone_label = ttk.Label(timings, text=device.zone, width=20)
            zone_label.grid(row=device.id, column=3, padx=5, pady=5, sticky="w")

            dropdown_on_value = tk.StringVar()
            dropdown_on_values[device.id] = dropdown_on_value
            current_on_choice: int = options.index(device.on)
            dropdown_on_menu = ttk.OptionMenu(
                timings,
                dropdown_on_value,
                options[current_on_choice],
                *options,
            )
            dropdown_on_menu.grid(row=device.id, column=4, padx=10, pady=5, sticky="w")
            dropdown_on_menus[device.id] = dropdown_on_menu

            dropdown_off_value = tk.StringVar()
            dropdown_off_values[device.id] = dropdown_off_value
            current_off_choice: int = options.index(device.off)
            dropdown_off_menu = ttk.OptionMenu(
                timings,
                dropdown_off_value,
                options[current_off_choice],
                *options,
            )
            dropdown_off_menu.grid(row=device.id, column=5, padx=10, pady=5, sticky="w")
            dropdown_off_menus[device.id] = dropdown_off_menu

        save_button = ttk.Button(
            timings,
            text="Save",
            command=lambda: save_devices_timings(timings, devices, callback),
        )
        save_button.grid(row=7, column=5, padx=2, pady=25, sticky="w")

        timings.mainloop()

    else:
        timings.focus_force()

def check_devices_timings(device: Device) -> bool:
    """
    Check whether the timings are correct.
    """
    time_on = device.on
    time_off = device.off
    error_text = None
    if time_on == time_off:
        error_text = "Error! The ON time is equal the OFF time!"
    if time_on and not time_off:
        error_text = "Error! The ON is set but the OFF is not set!"
    if error_text:
        messagebox.showerror("Error", error_text, parent=timings)
        return False

    return True


def save_devices_timings(
        _timings: tk.Toplevel,
        devices: list[Device],
        callback: callable,
) -> None:
    """
    Get the timings from the drop-down menus,
    Call the function to save the timings to the ".env" file.
    Close the timings window.
    """
    for device in devices:

        device.on = dropdown_on_values[device.id].get()
        device.off = dropdown_off_values[device.id].get()

        timings_are_correct = check_devices_timings(device)
        if not timings_are_correct:
            break
    else:
        save_devices_config(devices)
        _timings.destroy()

        callback(devices)


timings = None

import tkinter as tk
from tkinter import ttk

from entities import CommonTitles
from configs import read_description

settings = tk.Tk()
settings.title("Settings")
settings.geometry("1000x250")

description: CommonTitles = read_description()


def settings_window():

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

    for i in range(2, 6, 1):

        number_label = ttk.Label(settings)
        number_label.grid(row=i, column=0, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings)
        name_label.grid(row=i, column=1, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings)
        name_label.grid(row=i, column=2, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings)
        name_label.grid(row=i, column=3, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings)
        name_label.grid(row=i, column=4, padx=5, pady=10, sticky="w")

        name_label = ttk.Entry(settings)
        name_label.grid(row=i, column=5, padx=5, pady=10, sticky="w")



    settings.mainloop()


settings_window()

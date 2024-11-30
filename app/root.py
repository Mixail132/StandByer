import tkinter as tk
from tkinter import ttk
from equipment import load_config

items = load_config()
amps = []

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("750x200")


selected_values = {}

number = ttk.Label(root, text="1")
number.grid(row=1, column=0, padx=5, pady=5, sticky="w")

state_image = tk.PhotoImage(file="../img/green.png")
state = ttk.Label(root, image=state_image)
state.grid(row=1, column=1, padx=5, pady=5, sticky="w")

label = ttk.Label(root, text="AL1604D")
label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

label = ttk.Label(root, text="Каминный зал")
label.grid(row=1, column=3, padx=30, pady=5, sticky="w")

on_button = ttk.Radiobutton(root, text="on", value="on")
on_button.grid(row=1, column=4, padx=5, pady=5, sticky="w")

off_button = ttk.Radiobutton(root, text="off", value="off")
off_button.grid(row=1, column=5, padx=5, pady=5, sticky="w")

ok_button = ttk.Button(root, text="ok")
ok_button.grid(row=1, column=6, padx=40, pady=5, sticky="w")

progress_bar = ttk.Progressbar(root, orient="horizontal", length="200")
progress_bar.grid(row=1, column=7, padx=5, pady=5, sticky="w")

root.mainloop()

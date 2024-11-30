import tkinter as tk
from tkinter import ttk
from equipment import load_config

amps = []

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("750x200")

selected_values = {}

for num in range(1, 6):

    number = ttk.Label(root, text=num)
    number.grid(row=num, column=0, padx=5, pady=5, sticky="w")

    state_image = tk.PhotoImage(file="../img/green.png")
    state = ttk.Label(root, image=state_image)
    state.grid(row=num, column=1, padx=5, pady=5, sticky="w")

    label = ttk.Label(root, text="AL1604D")
    label.grid(row=num, column=2, padx=5, pady=5, sticky="w")

    label = ttk.Label(root, text="Fireplace room")
    label.grid(row=num, column=3, padx=30, pady=5, sticky="w")

    on_button = ttk.Radiobutton(root, text="on", value="on")
    on_button.grid(row=num, column=4, padx=5, pady=5, sticky="w")

    off_button = ttk.Radiobutton(root, text="off", value="off")
    off_button.grid(row=num, column=5, padx=5, pady=5, sticky="w")

    ok_button = ttk.Button(root, text="ok")
    ok_button.grid(row=num, column=6, padx=40, pady=5, sticky="w")

    progress_bar = ttk.Progressbar(root, orient="horizontal", length="200")
    progress_bar.grid(row=num, column=7, padx=5, pady=5, sticky="w")

root.mainloop()

import tkinter as tk
from equipment import load_config

items = load_config()
amps = []

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("600x200")

for item in items:
    amps.append(item.name)

selected_values = {}

for num, amp in enumerate(amps, 1):
    label = tk.Label(root, text=amp)
    label.grid(row=num, column=0, padx=5, pady=5, sticky="w")

    var = tk.StringVar(value="on")  # Here sets the default value
    selected_values[amp] = var

    on_button = tk.Radiobutton(root, text="on", variable=var, value="on")
    on_button.grid(row=num, column=1, padx=5, pady=5, sticky="w")

    off_button = tk.Radiobutton(root, text="off", variable=var, value="off")
    off_button.grid(row=num, column=2, padx=5, pady=5, sticky="w")


root.mainloop()

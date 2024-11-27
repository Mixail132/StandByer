import tkinter as tk
from equipment import load_config

items = load_config()
amps = []

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("600x600")

for item in items:
    amps.append(item.name)

for amp in amps:
    label = tk.Label(root, text=amp)
    label.pack(anchor="w", padx=10, pady=10)

root.mainloop()

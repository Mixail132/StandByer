import tkinter as tk
from tkinter import ttk
from actions import get_mock_state

amps = get_mock_state()

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("750x200")


def set_standby(amp_ip):
    selected_value = selected_values[amp_ip].get()
    print(f"{amp.ip} set standby: {selected_value}")


selected_values = {}

for num, amp in enumerate(amps, 1):

    number_label = ttk.Label(root, text=num)
    number_label.grid(row=num, column=0, padx=5, pady=5, sticky="w")

    state_image = tk.PhotoImage(file=amp.mark)
    state_label = ttk.Label(root, image=state_image)
    state_label.image = state_image
    state_label.grid(row=num, column=1, padx=5, pady=5, sticky="w")

    type_label = ttk.Label(root, text=amp.type)
    type_label.grid(row=num, column=2, padx=5, pady=5, sticky="w")

    zone_label = ttk.Label(root, text=amp.zone)
    zone_label.grid(row=num, column=3, padx=30, pady=5, sticky="w")

    var = tk.StringVar(value=amp.standby)
    selected_values[amp.ip] = var
    on_button = ttk.Radiobutton(root, text="on", value="on", variable=var)
    on_button.grid(row=num, column=4, padx=5, pady=5, sticky="w")

    off_button = ttk.Radiobutton(root, text="off", value="off", variable=var)
    off_button.grid(row=num, column=5, padx=5, pady=5, sticky="w")

    ok_button = ttk.Button(root, text="ok", command=lambda ip=amp.ip: set_standby(ip))
    ok_button.grid(row=num, column=6, padx=40, pady=5, sticky="w")

    progress_bar = ttk.Progressbar(root, orient="horizontal", length="200")
    progress_bar.grid(row=num, column=7, padx=5, pady=5, sticky="w")

root.mainloop()

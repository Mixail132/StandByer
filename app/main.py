import tkinter as tk

root = tk.Tk()
root.title("Amplifiers' switcher")
root.geometry("600x600")

listbox = tk.Listbox(root)
elements = ["el1", "el2", "el3"]
listbox.pack(fill=tk.BOTH, expand=True)

for element in elements:
    amplifier = tk.Radiobutton(text=element, value=element)
    amplifier.pack()

root.mainloop()

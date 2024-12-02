"""Widgets' pop-up windows handling."""
from entities import DeviceConfig, CommonTitles
from configs import read_description
import tkinter as tk

class ToolTip:
    """
    Handles a pop-up window to a widget.
    """

    def __init__(self, widget, text):
        """
        Initializes the pop-up window settings.
        """
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        """Shows the pop-up window."""
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            font=("tahoma", "8", "normal")
        )
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        """Hides thr pop-up window."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


def get_tooltip(
        devices: list[DeviceConfig],
) -> list[DeviceConfig]:
    """Combines the pop-up text."""
    descriptions = []
    title: CommonTitles = read_description()

    for device in devices:
        device.description = f"""
        {title.description}:
        •  {title.name}:    {device.name}
        •  {title.type}:    {device.type}
        •  {title.zone}:    {device.zone}
        •  {title.ip}:      {device.ip}
        •  {title.place}:   {device.place}
        •  {title.state}:   {device.state}
        """
        descriptions.append(device)

    return descriptions

"""Widgets' pop-up windows handling."""

from app.entities import Device, Description
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
        padding = 15
        x += self.widget.winfo_rootx() + padding
        y += self.widget.winfo_rooty() + padding

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
        label.pack(ipadx=padding, ipady=padding)

    def hide_tooltip(self, event):
        """Hides thr pop-up window."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


def set_info_tooltip(
        devices: list[Device],
        titles: Description
) -> list[Device]:
    """Combines the pop-up info text."""

    states = {0: titles.on, 1: titles.standby, -1: titles.out}
    for device in devices:
        device.description = f"""
        {titles.description}:
        •  {titles.name}:  {device.name}
        •  {titles.type}:  {device.type}
        •  {titles.zone}:  {device.zone}
        •  {titles.ip}:  {device.ip}
        •  {titles.place}:  {device.place}
        •  {titles.state}:  {states[device.state]}
        """

    return devices


def set_timing_tooltip(
        devices: list[Device],
) -> list[Device]:
    """Combines the pop-up timing text."""

    for device in devices:
        device.schedule = f"""
        •  ON  :  {device.on}
        •  OFF :  {device.off}
        """

    return devices

import requests
import random

from entities import Device
from payloads import get_payload


def check_states(devices: list[Device]) -> list[Device]:
    """
    Check the devices' current state.
    """
    payload = get_payload(action="READ")
    states = []

    for device in devices:
        url = f"http://{device.ip}/am"
        headers = {"Content-Type": "application/json"}

        device.state = -1
        response = requests.post(url, headers=headers, json=payload)

        if response.ok:
            data = response.json()
            device.state = data["payload"]["action"]["values"][0]["data"]
        states.append(device)

    return states


def set_real_state(
        device_ip: str,
        standby_mode: bool,
) -> bool | None:
    """
    Change the device's standby mode.
    :param device_ip: the device's IP to be changed.
    :param standby_mode: True - to set standby mode.
    :return: the command result:
        True, False - the command succeed, the state has changed.
        None - the command is unsuccessful, the device is unreached.
    """
    payload = get_payload(action="WRITE", standby_mode=standby_mode)
    url = f"http://{device_ip}/am"
    headers = {"Content-Type": "application/json"}

    command_status: bool | None = None
    try:
        response = requests.post(url, headers=headers, json=payload)
    except requests.exceptions.ConnectTimeout:
        ...
        # Add a logic the device became unreached/
        return None

    if response.ok:
        data = response.json()
        command_status = data["payload"]["action"]["values"][0]["data"]["boolValue"]

    return command_status


def set_random_states(devices: list[Device]) -> list[Device]:
    """
    Set the random states to the devices for initials.
    """
    states = []

    for device in devices:

        random_state = random.choice([-1, 1, 0])
        device.state = random_state
        device = set_state_mark(device)
        states.append(device)

    return states


def set_state_mark(device: Device) -> Device:
    """
    Set the mark depending on the device state.
    """
    if device.state == 0:
        device.mark = "../img/red.png"
        device.standby = "on"

    elif device.state == 1:
        device.mark = "../img/green.png"
        device.standby = "off"

    return device

import requests
import random

from entities import Device
from payloads import get_payload


def check_states(devices: list[Device]) -> list[Device]:
    """
    Checks the devices' current state.
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


def check_state(
        device_ip: str,
        standby_mode: bool = True,
) -> bool | None:
    """
    Sets the devices' standby mode.
    :param device_ip: the device's IP to be changed
    :param standby_mode: True - to set standby
    :return: the command result:
        True, False - the command succeed, the state has changed.
        None - the command is unsuccessful, the device is unreached.
    """
    payload = get_payload(action="WRITE", standby_mode=standby_mode)
    url = f"http://{device_ip}/am"
    headers = {"Content-Type": "application/json"}

    command_status: bool | None = None
    response = requests.post(url, headers=headers, json=payload)

    if response.ok:
        data = response.json()
        command_status = data["payload"]["action"]["values"][0]["data"]["boolValue"]

    return command_status


def set_random_state(devices: list[Device]) -> list[Device]:
    """
    Sets the random states to the devices for initials.
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
    Sets the mark depending on the device state.
    """

    if device.state == 0:
        device.mark = "../img/red.png"
        device.standby = "on"

    elif device.state == 1:
        device.mark = "../img/green.png"
        device.standby = "off"

    return device

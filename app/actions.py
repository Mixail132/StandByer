"""
This module provides actions to check the devices' states,
set the devices states and set their state marks.
"""

import random

import requests
from requests.exceptions import ConnectionError as RequestConnectionError
from requests.exceptions import ConnectTimeout

from app.dirs import DIR_IMG
from app.entities import Device
from app.payloads import get_payload


def check_devices_states(devices: list[Device]) -> list[Device]:
    """
    Check the devices' current state.
    """
    payload = get_payload(action="READ")
    states = []

    for device in devices:
        url = f"http://{device.ip}/am"
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=2)
            if response.ok:
                data = response.json()
                device.state = data["payload"]["action"]["values"][0]["data"]['intValue']

        except (ConnectTimeout, RequestConnectionError):
            device.state = -1

        states.append(device)

    return states


def set_real_state(
        device_ip: str,
        standby_mode: bool,
) -> str:
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

    command_result: str = "Unreached"
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=2)
    except (ConnectTimeout, RequestConnectionError):
        return command_result

    if response.ok:
        data = response.json()
        payload_result = data["payload"]["action"]["values"][0]["data"]["boolValue"]

        if payload_result is True:
            command_result = "Standby"
        elif payload_result is False:
            command_result = "Active"

    return command_result


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
    Set the color circle mark depending on the device state.
    Set the device standby mode depending on the device state.
    """
    if device.state == 0:
        device.mark = DIR_IMG / "red.png"
        device.standby = "on"

    elif device.state == 1:
        device.mark = DIR_IMG / "green.png"
        device.standby = "off"

    elif device.state == -1:
        device.mark = DIR_IMG / "grey.png"
        device.standby = None

    return device


def set_clock_mark(device: Device) -> Device:
    """
    Set a device's schedule color clock mark.
    Keep it in special variable.
    """

    if device.on == "-- :--" and device.off == "-- :--":
        device.timing = False
        device.clock = DIR_IMG / "noclock.png"
    else:
        device.timing = True
        device.clock = DIR_IMG / "clock.png"

    return device

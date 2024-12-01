import requests
import random

from configs import read_config
from entities import AmplifierConfig
from payloads import get_payload


def check_state() -> list[AmplifierConfig]:
    """
    Checks the amplifiers' current state.
    """
    amplifiers = read_config()
    payload = get_payload(action="READ")
    states = []

    for amplifier in amplifiers:
        url = f"http://{amplifier.ip}/am"
        headers = {"Content-Type": "application/json"}

        amplifier.state = -1
        response = requests.post(url, headers=headers, json=payload)

        if response.ok:
            data = response.json()
            amplifier.state = data["payload"]["action"]["values"][0]["data"]
        states.append(amplifier)

    return states


def set_state(
        amplifier_ip: str,
        standby_mode: bool = True,
) -> bool | None:
    """
    Sets the amplifiers' standby mode.
    :param amplifier_ip: the amplifier's IP to be changed
    :param standby_mode: True - to set standby
    :return: the command result:
        True, False - the command succeed, the state has changed.
        None - the command is unsuccessful,  amplifier is unreached.
    """
    payload = get_payload(action="WRITE", standby_mode=standby_mode)
    url = f"http://{amplifier_ip}/am"
    headers = {"Content-Type": "application/json"}

    command_status: bool | None = None
    response = requests.post(url, headers=headers, json=payload)

    if response.ok:
        data = response.json()
        command_status = data["payload"]["action"]["values"][0]["data"]["boolValue"]

    return command_status


def get_mock_state() -> list[AmplifierConfig]:
    amplifiers = read_config()
    states = []

    for amplifier in amplifiers:

        amplifier.state = -1

        amplifier.state = random.choice([-1, 1, 0])
        states.append(amplifier)
        states = set_state_mark(states)

    return states


def set_state_mark(devices: list[AmplifierConfig]) -> list[AmplifierConfig]:
    """
    Sets the mark depending on the device state.
    """

    for device in devices:

        if device.state == 0:
            device.mark = "../img/red.png"
            device.standby = "on"

        elif device.state == 1:
            device.mark = "../img/green.png"
            device.standby = "off"

    return devices

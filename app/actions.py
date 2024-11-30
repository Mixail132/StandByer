import requests
from entities import AmplifierConfig
from payloads import get_payload
from configs import read_config


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
    :return:
    """
    payload = get_payload(action="WRITE", standby_mode=standby_mode)
    url = f"http://{amplifier_ip}/am"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=payload)
    command_status: bool | None = None
    if response.ok:
        data = response.json()
        command_status = data["payload"]["action"]["values"][0]["data"]["boolValue"]

    return command_status

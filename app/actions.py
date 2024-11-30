import requests
from entities import AmplifierConfig
from environs import Env
from payloads import get_payload


def read_config() -> list[AmplifierConfig]:
    """
    Reads the amplifiers' descriptions from the .env file.
    """
    env: Env = Env()
    env.read_env(".env")
    amplifiers = []

    for num in range(1, 6):
        amplifier = AmplifierConfig(
            type=env.str(f"A{num}_TYPE"),
            ip=env.str(f"A{num}_IP"),
            zone=env.str(f"{num}_ZONE"),
            place=env.str(f"{num}_PLACE")
        )
        amplifiers.append(amplifier)

    return amplifiers


def check_state(self) -> list[AmplifierConfig]:
    """
    Checks the amplifiers' current state.
    """
    amplifiers = self.read_config()
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

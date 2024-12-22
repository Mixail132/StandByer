"""
A payload to include in the HTTP request to the device
to change or read the device's state.
"""

def get_payload(
        standby_mode: bool | None = None,
        action: str = "READ",
) -> dict:

    client_id: str = "x8-panel"
    endpoint: str = "/Device/Audio/Presets/Live/Generals/Standby/Value"
    values: list = [{"id": endpoint, "single": True}]

    if action == "WRITE":
        values = [
            {
                "id": endpoint,
                "data": {"type": "BOOL", "boolValue": standby_mode},
            }
        ]

    return {
        "clientId": client_id,
        "payload": {
            "type": "ACTION",
            "action": {"type": action, "values": values}
        }
    }

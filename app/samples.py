"""
Actual request payloads for the devices
for which the project is developed.
"""

set_standby_on_request_payload = {
    "clientId": "x8-panel",
    "payload": {
        "type": "ACTION", "action": {
            "type": "WRITE",
            "values": [
                {
                    "id": "/Device/Audio/Presets/Live/Generals/Standby/Value",
                    "data": {
                        "type": "BOOL",
                        "boolValue": True
                    }
                }
            ]
        }
    }
}

set_standby_off_request_payload = {
    "clientId": "x8-panel",
    "payload": {
        "type": "ACTION",
        "action": {
            "type": "WRITE",
            "values": [
                {
                    "id": "/Device/Audio/Presets/Live/Generals/Standby/Value",
                    "data": {
                        "type": "BOOL",
                        "boolValue": False
                    }
                }
            ]
        }
    }
}


get_state_request_payload = {
    "clientId": "x8-panel",
    "payload": {
        "type": "ACTION",
        "action": {
            "type": "READ",
            "values": [
                {
                    "id": "/Device/Audio/Presets/Live/Generals/Standby/Value",
                    "single": True
                }
            ]
        }
    }
}



from entities import PayloadConfig
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

CLIENT_ID = "x8-panel"
TYPE = "READ"
SINGLE = "true"
ID = "/Device/Audio/Presets/Live/Generals/Standby/Value"
BOOLVALUE = "false"

class AmplifierRequestPayload:

    @staticmethod
    def get_state_payload(payload: PayloadConfig):
        return {
            "clientId": payload.client_id,
            "payload": {
                "type": "ACTION",
                "action": {
                    "type": "READ",
                    "values": [
                        {
                            "id": payload.id,
                            "single": payload.single,
                        }
                    ]
                }
            }
        }

    def set_standby_payload(
            self,
            payload: PayloadConfig,
            standby_mode: bool,
    ):
        return {
            "clientId": payload.client_id,
            "payload": {
                "type": "ACTION",
                "action": {
                    "type": "WRITE",
                    "values": [
                        {
                            "id": payload.id,
                            "data": {
                                "type": "BOOL",
                                "boolValue": standby_mode
                            },
                        }
                    ]
                }
            }
        }



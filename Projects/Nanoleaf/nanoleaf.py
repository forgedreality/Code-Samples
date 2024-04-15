class Nanoleaf:
    def __init__(self, ip, auth_token, name, checked_by_default=True, ids=[], offset_ids=[]):
        self.ip = ip
        self.token = auth_token
        self.name = name
        self.checked_by_default = checked_by_default

        self.ids = ids
        self.offset_ids = offset_ids

        # endpoints
        self.endpoints = {
            "state": "state",
            "effects": "effects",
            "effectsList": "effects/effectsList",
            "layout": "panelLayout/layout"
        }

    # def get_endpoints(self):
    #     return self.endpoints

    # should set IDs on instantiation
    def set_ids(self, data):
        self.ids = data

import json

VERSION_NUM = 0x00

class Datagram:
    def __init__(self, version: int, data: str, game_id: int, user_id: int, itype: int):
        self.version = version
        self.data = data
        self.game_id = game_id
        self.user_id = user_id
        self.itype = itype

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        return Datagram(**json.loads(json_str))

    def to_bytes(self):
        return json.dumps(self.__dict__).encode('utf-8')

    @staticmethod
    def from_bytes(json_bytes):
        return Datagram(**json.loads(json_bytes.decode('utf-8')))

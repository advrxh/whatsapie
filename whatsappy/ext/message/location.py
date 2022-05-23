from whatsappy.ext.message import Message


class LocationMessage(Message):
    def __init__(
        self,
        to: str,
        long: str = None,
        lat: str = None,
        name: str = None,
        address: str = None,
    ):
        self.set_params(long=long, lat=lat, name=name, address=address)
        super().__init__(to=to)

    def set_params(self, long: str, lat: str, name: str, address: str):
        self.long = long
        self.lat = lat
        self.name = name
        self.address = address

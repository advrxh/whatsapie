from whatsapie.ext.message.message import Message


class LocationMessage(Message):
    """Inherits from Message class.

    Inherits from Message class, represents a Location Message api object.

    Args:
        long: Longitude value
        lat: Latitude value.
        name: Name of the location.
        address: Address of the location.
    """

    def __init__(
        self,
        long: str = None,
        lat: str = None,
        name: str = None,
        address: str = None,
        to: str = None,
    ):
        self.set_params(long=long, lat=lat, name=name, address=address)
        super().__init__(to=to)

    def set_params(self, long: str, lat: str, name: str, address: str):
        """Sets the values of parameters to the respective class instances.
        Args:
            long: Longitude value
            lat: Latitude value.
            name: Name of the location.
            address: Address of the location.
        """
        self.long = long
        self.lat = lat
        self.name = name
        self.address = address

class Location:
    """
    Whatsapp message Location object class
    """

    def __init__(self, long: str, lat: str, name: str, address: str):
        self.long = long
        self.lat = lat
        self.name = name
        self.address = address

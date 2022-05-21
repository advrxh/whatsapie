from whatsapy.api_objects.text import Text
from whatsapy.api_objects.location import Location
from whatsapy.api_objects.media import Media


class Message:
    """
    Whatsapi Message object class
    """

    def __init__(self, to: str) -> None:
        self.to = to

        self.text = None
        self.location = None
        self.media = None
        self.media_order = "before"

    def set_text(self, text: Text):
        self.text = text

    def set_location(self, location: Location):
        self.location = location

    def set_media(self, media: Media):
        self.media = media

    def set_media_order(self, order):
        if order not in ["before", "after"]:
            return
        self.media_order = order

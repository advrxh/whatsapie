import json

from whatsapy.api_objects import Message
from whatsapy.body_generator.format_text import format_text
from whatsapy.body_generator.format_location import format_location


class BodyGenerator:
    """
    Whatsapi BodyGenerator. Takes in native python object class and converts it into json api bodies.
    """

    def __init__(self):
        pass

    def generate(
        self,
        message: Message,
        dump_json_str: bool = True,
    ):
        body = {"messaging_product": "whatsapp", "recipient_type": "individual"}
        body["to"] = message.to

        if message.text is not None:
            body = format_text(body, message)

        if message.location is not None:
            body = format_location(body, message)

        if dump_json_str:
            return self.dump_json(body)

        return body

    def generate_media_body(self, message: Message, dump_json_str: bool = True):
        body = {"messaging_product": "whatsapp", "recipient_type": "individual"}

        body["to"] = message.to
        body["type"] = message.media.type
        body[message.media.type] = {"link": message.media.link}

        if message.media.type in ["document", "image"] and message.media.caption:
            body[message.media.type]["caption"] = message.media.caption

        if message.media.type == "document" and message.media.filename:
            body[message.media.type]["filename"] = message.media.filename

        if dump_json_str:
            return self.dump_json(body)

        return body

    def dump_json(self, body):
        return json.dumps(body)

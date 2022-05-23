import json

from whatsappy.ext import Message, TextMessage, LocationMessage, MediaMessage

from whatsappy.schema_generator.text_schema import generate_text_schema
from whatsappy.schema_generator.location_schema import generate_location_schema
from whatsappy.schema_generator.media_schema import generate_media_schema


class SchemaGenerator:
    """
    Schema generator class, that generated api body schemas according to
    provided arguments of type Message.
    """

    def __init__(self):
        pass

    def generate(
        self,
        message: Message,
        dump_json_str: bool = True,  # If set to True returns a stringified version of the dict object
    ):
        """
        Generates schema for the provided message argument.
        """
        body = {"messaging_product": "whatsapp", "recipient_type": "individual"}
        body["to"] = message.to

        if isinstance(message, TextMessage):
            body = generate_text_schema(body, message)

        if isinstance(message, LocationMessage):
            body = generate_location_schema(body, message)

        if isinstance(message, MediaMessage):
            body = generate_media_schema(body, message)

        if dump_json_str:
            return self.dump_json(body)

        return body

    def dump_json(self, body):
        """
        Convert native python dictionary to a stringified json.
        """
        return json.dumps(body)

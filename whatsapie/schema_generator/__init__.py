import json

from whatsapie.ext import Message, Text, Location, Media, Template, ContactGroup

from whatsapie.schema_generator.text_schema import generate_text_schema
from whatsapie.schema_generator.location_schema import generate_location_schema
from whatsapie.schema_generator.media_schema import generate_media_schema
from whatsapie.schema_generator.template_schema import generate_template_schema
from whatsapie.schema_generator.contact_schema import generate_contact_group_schema


class SchemaGenerator:
    """Generates api schema from native python object classes.

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
        """Generates schema for the provided message argument.

        Args:
            message: Must be a type of Message Instance supports **Text, Location, Media**.
            dump_json_str: When set to false, will return native python dict.

        Returns:
            body: if dump_json_str is True, returns stringified json, else returns native python dict.
        """
        body = {"messaging_product": "whatsapp", "recipient_type": "individual"}
        body["to"] = message.to

        if isinstance(message, Text):
            body = generate_text_schema(body, message)

        if isinstance(message, Location):
            body = generate_location_schema(body, message)

        if isinstance(message, Media):
            body = generate_media_schema(body, message)

        if isinstance(message, Template):
            body = generate_template_schema(body, message)

        if isinstance(message, ContactGroup):
            body = generate_contact_group_schema(body, message)

        if dump_json_str:
            return self.dump_json(body)

        return body

    def dump_json(self, body):
        return json.dumps(body)

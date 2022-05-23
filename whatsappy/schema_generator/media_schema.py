from whatsappy.ext.message import MediaMessage
from whatsappy.constants import (
    CAPTION_ALLOWED_MEDIA_TYPES,
    FILENAME_ALLOWED_MEDIA_TYPES,
)


def generate_media_schema(body: dict, message: MediaMessage):
    body["type"] = message.type
    body[message.type] = {"link": message.link}

    if message.type in CAPTION_ALLOWED_MEDIA_TYPES:
        body[message.type]["caption"] = message.caption

    if message.type in FILENAME_ALLOWED_MEDIA_TYPES:
        body[message.type]["filename"] = message.filename

    return body

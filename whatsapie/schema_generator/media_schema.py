from whatsapie.constants import (CAPTION_ALLOWED_MEDIA_TYPES,
                                 FILENAME_ALLOWED_MEDIA_TYPES)
from whatsapie.ext.message import Media


def generate_media_schema(body: dict, message: Media):
    """Generate schema for Media.

    Args:
        body: Parent api schema object.
        message: Media instance.

    Returns:
        body: Schema body
    """
    body["type"] = message.type
    body[message.type] = {"link": message.link}

    if message.type in CAPTION_ALLOWED_MEDIA_TYPES:
        body[message.type]["caption"] = message.caption

    if message.type in FILENAME_ALLOWED_MEDIA_TYPES:
        body[message.type]["filename"] = message.filename

    return body

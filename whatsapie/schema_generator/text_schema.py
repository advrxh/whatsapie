from whatsapie.ext.message import Text


def generate_text_schema(body: dict, message: Text):
    """Generate schema for Text.

    Args:
        body: Parent api schema object.
        message: Text instance.

    Returns:
        body: Schema body
    """
    body["type"] = "text"
    body["text"] = {"preview_url": message.preview_url, "body": message.body}

    return body

from whatsappy.ext.message import TextMessage


def generate_text_schema(body: dict, message: TextMessage):
    """Generate schema for TextMessage.

    Args:
        body: Parent api schema object.
        message: TextMessage instance.

    Returns:
        body: Schema body
    """
    body["type"] = "text"
    body["text"] = {"preview_url": message.preview_url, "body": message.body}

    return body

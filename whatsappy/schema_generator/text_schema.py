from whatsappy.ext.message import TextMessage


def generate_text_schema(body: dict, message: TextMessage):
    body["type"] = "text"
    body["text"] = {"preview_url": message.preview_url, "body": message.body}

    return body

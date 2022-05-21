from whatsapy.api_objects import Message


def format_text(body: dict, message: Message):
    body["type"] = "text"
    body["text"] = {"preview_url": message.text.preview_url, "body": message.text.body}

    return body

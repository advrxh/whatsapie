from whatsapy.api_objects import Message


def format_location(body: dict, message: Message):
    body["type"] = "location"
    body["location"] = {
        "longitude": message.location.long,
        "latitude": message.location.lat,
        "name": message.location.name,
        "address": message.location.address,
    }

    return body

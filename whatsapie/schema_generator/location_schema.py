from whatsapie.ext.message import LocationMessage


def generate_location_schema(body: dict, message: LocationMessage):
    """Generate schema for LocationMessage.

    Args:
        body: Parent api schema object.
        message: LocationMessage instance.

    Returns:
        body: Schema body
    """
    body["type"] = "location"
    body["location"] = {
        "longitude": message.long,
        "latitude": message.lat,
        "name": message.name,
        "address": message.address,
    }

    return body

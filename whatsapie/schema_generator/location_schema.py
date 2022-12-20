from whatsapie.ext.message import Location


def generate_location_schema(body: dict, message: Location):
    """Generate schema for Location.

    Args:
        body: Parent api schema object.
        message: Location instance.

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

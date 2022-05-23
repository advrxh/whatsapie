from whatsappy.ext.message import LocationMessage


def generate_location_schema(body: dict, message: LocationMessage):
    body["type"] = "location"
    body["location"] = {
        "longitude": message.long,
        "latitude": message.lat,
        "name": message.name,
        "address": message.address,
    }

    return body

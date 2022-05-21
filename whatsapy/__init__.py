import requests as rq

from whatsapy.api_objects import *
from whatsapy.body_generator import BodyGenerator
from whatsapy.errors import ErrorResponse, ErrorMediaResponse


class Whatsapy:
    """
    Whatsapp Cloud API main wrapper class.
    """

    def __init__(self, access_token: str, phone_number_id: str) -> None:
        self.body_generator = BodyGenerator()
        self.access_token = access_token

        self.phone_number_id = phone_number_id

        self.url = f"https://graph.facebook.com/v13.0/{self.phone_number_id}/messages"

    def push(self, message: Message):
        body = self.body_generator.generate(message, dump_json_str=True)
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        if message.media_order == "before":
            self.push_media(message)
            response = rq.post(self.url, headers=headers, data=body)

        elif message.media_order == "after":
            response = rq.post(self.url, headers=headers, data=body)
            self.push_media(message)

        if response.status_code == 200:
            return True

        raise ErrorResponse(response)

    def push_media(self, message: Message):
        body = self.body_generator.generate_media_body(message)
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        response = rq.post(self.url, data=body, headers=headers)

        if response.status_code == 200:
            return True

        raise ErrorMediaResponse(response)

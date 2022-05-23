import requests as rq

from whatsappy.ext.message import *
from whatsappy.schema_generator import SchemaGenerator
from whatsappy.errors import ErrorResponse
from whatsappy.constants import (
    META_GRAPH_API_ENDPOINT,
    META_GRAPH_API_VERSION,
    REQUEST_HEADERS,
)


class Whatsappy:
    """
    Whatsapp Cloud API main wrapper class.
    """

    def __init__(self, access_token: str, phone_number_id: str) -> None:
        self.schema_generator = SchemaGenerator()
        self.access_token = access_token
        self.phone_number_id = phone_number_id

        self.url = META_GRAPH_API_ENDPOINT.format(
            version=META_GRAPH_API_VERSION, phone_number_id=self.phone_number_id
        )

    def send(self, message: Message):
        body = self.schema_generator.generate(message, dump_json_str=True)
        headers = REQUEST_HEADERS
        headers["Authorization"] = f"Bearer {self.access_token}"

        print(body)

        response = rq.post(self.url, headers=headers, data=body)

        if response.status_code == 200:
            return True

        raise ErrorResponse(response)

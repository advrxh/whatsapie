import requests as rq

from whatsapie.ext.message import *
from whatsapie.schema_generator import SchemaGenerator
from whatsapie.errors import ErrorResponse
from whatsapie.constants import (
    META_GRAPH_API_ENDPOINT,
    META_GRAPH_API_VERSION,
    REQUEST_HEADERS,
)


class Whatsapie:
    """
    Whatsapp Cloud API manager class, this class handles the functions of making
    requests to Meta's cloud api.
    """

    def __init__(self, access_token: str, phone_number_id: str) -> None:
        """Initializes the whatsapie manager class.

        Args:
            access_token: Meta's Whatsapp Cloud API user specific access token.
            phone_number_id: Meta's Whatsapp Cloud API user specific phone number ID.

        """
        self.schema_generator = SchemaGenerator()
        self.access_token = access_token
        self.phone_number_id = phone_number_id

        self.url = META_GRAPH_API_ENDPOINT.format(
            version=META_GRAPH_API_VERSION, phone_number_id=self.phone_number_id
        )

    def send(self, message: Message):
        """Invoke this method from an instance to send a whatsapp message

        Args:
            message: Must be a type of Message Instance supports **TextMessage, LocationMessage, MediaMessage**

        Returns:
            A bool status of the performed api call

        Raises:
            ErrorResponse: If the Cloud API returns and error response
        """
        body = self.schema_generator.generate(message, dump_json_str=True)
        headers = REQUEST_HEADERS
        headers["Authorization"] = f"Bearer {self.access_token}"

        response = rq.post(self.url, headers=headers, data=body)

        if response.status_code == 200:
            return True

        raise ErrorResponse(response)

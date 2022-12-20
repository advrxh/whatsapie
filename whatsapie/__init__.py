import asyncio
from pprint import pprint

import httpx
from loguru import logger

from whatsapie.constants import (META_GRAPH_API_ENDPOINT,
                                 META_GRAPH_API_VERSION, REQUEST_HEADERS)
from whatsapie.errors import ErrorResponse
from whatsapie.ext.message import *
from whatsapie.schema_generator import SchemaGenerator


class Whatsapie:
    """
    Whatsapp Cloud API manager class, this class handles the functions of making
    httpx to Meta's cloud api.
    """

    def __init__(self, access_token: str, phone_number_id: str, log:bool=False) -> None:
        """Initializes the whatsapie manager class.

        Args:
            access_token: Meta's Whatsapp Cloud API user specific access token.
            phone_number_id: Meta's Whatsapp Cloud API user specific phone number ID.

        """
        self.schema_generator = SchemaGenerator()
        self.access_token = access_token
        self.phone_number_id = phone_number_id
        self.log = log

        self.url = META_GRAPH_API_ENDPOINT.format(
            version=META_GRAPH_API_VERSION, phone_number_id=self.phone_number_id
        )

    def inspect_schema(self, message: Message, pretty_print: bool = True):
        """Invoke this method from an instance to inspect the api schema of this message


        Args:
            message: Must be a type of Message Instance supports **Text, Location, Media**
        """

        body = self.schema_generator.generate(message, dump_json_str=False)

        if not pretty_print:
            return body

        pprint(body, depth=2, width=4)
        return body

    async def send(self, message: Message):
        """Invoke this method from an instance to send a whatsapp message

        Args:
            message: Must be a type of Message Instance supports **TextMessage, LocationMessage, MediaMessage**

        Returns:
            A bool status of the performed api call

        Raises:
            ErrorResponse: If the Cloud API returns and error response
        """


        async with httpx.AsyncClient(base_url=self.url) as client:
            await self.post(client=client, message=message)

    async def post(self, client, message):
        body = self.schema_generator.generate(message, dump_json_str=True)

        headers = REQUEST_HEADERS
        headers["Authorization"] = f"Bearer {self.access_token}"

        response = await client.post(url="/", data=body, headers=headers)

        if response.status_code == 200:
            if self.log:
                logger.info(f"OK | {response.status_code} | {response.text}") 
            return True

        raise ErrorResponse(response)

    async def send_group(self, message_group:MessageGroup):

        async with httpx.AsyncClient(base_url=self.url) as client:
            tasks = []
            for message in message_group.message_list:
                tasks.append(
                    asyncio.create_task(self.post(client=client, message=message))
                )

            await asyncio.gather(*tasks)
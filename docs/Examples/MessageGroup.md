## Message Groups

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, TextMessage, MessageGroup, LocationMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message_1 = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world"
)

text_message_2 = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world"
)

location_message = LocationMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    lat="LATITUDE_VALUE", # a decimal value, but pass parameter as a string
    long="LONGITUDE_VALUE", # a decimal value, but pass parameter as a string
    name="LOCATION_NAME", # location name
    address="LOCATION_ADDRESS" # location address

)

message_group = MessageGroup([text_message_1, text_message_2, location_message])

async def main():
    await manager.send_group(message_group)

asyncio.run(main())

```

## Message group to a single recipient

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, TextMessage, MessageGroup, LocationMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message_1 = TextMessage(
    body="Hello world"
)

text_message_2 = TextMessage(
    body="Hello world"
)

location_message = LocationMessage(
    lat="LATITUDE_VALUE", # a decimal value, but pass parameter as a string
    long="LONGITUDE_VALUE", # a decimal value, but pass parameter as a string
    name="LOCATION_NAME", # location name
    address="LOCATION_ADDRESS" # location address
)

message_group = MessageGroup(to="91XXXXXXXXXX",
                             message_list=[text_message_1, text_message_2, location_message])

async def main():
    await manager.send_group(message_group)

asyncio.run(main())

```

## Basic Location Message

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, LocationMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

location_message = LocationMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    lat="LATITUDE_VALUE", # a decimal value, but pass parameter as a string
    long="LONGITUDE_VALUE", # a decimal value, but pass parameter as a string
    name="LOCATION_NAME", # location name
    address="LOCATION_ADDRESS" # location address

)

async def main():
    await manager.send(location_message)

asyncio.run(main())

```

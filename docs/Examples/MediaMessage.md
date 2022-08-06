### Basic Media Message

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, MediaMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

location_message = MediaMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    type="media_type", # Media type, Supports 'image', 'audio', 'document', 'video'
    link="media_link", # Link to the hosted media on the web.
    caption="media_caption",
    filename="media_filename"

)

async def main():
    await manager.send(media_message)

asyncio.run(main())

```

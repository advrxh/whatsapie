## Basic Text Message

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())

```

## Basic Text Message with url preview

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world, https://helloworld.com",
    preview_url=True
)

async def main():
    await manager.send(text_message)

asyncio.run(main())

```

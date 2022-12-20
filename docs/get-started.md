whatsapie, The first wrapper for Meta's Whatsapp cloud API. Before you begin, you must first obtain the [ACCESS_TOKEN](#) and [PHONE_NUMBER_ID](#), which are given in the [Prerequisites](/whatsapie/#prerequisites).

!!! note "Using ENV variables for security"

    Using `os.getenv()`, load the environment variables ACCESS TOKEN and PHONE NUMBER ID into the module

Here's how to use whatsapie to send a short hello world message to a Whatsapp subscriber in 15 lines!!!!

```py title="hello_world.py" linenums="1"
import asyncio

from whatsapie import Whatsapie, Text

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = Text(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())
```

This is how simple it is to use whatsapie to send a hello world message. 🥳

## Closer Look!

Let's take a closer look at what's happening!

```py title="hello_world.py" linenums="1" hl_lines="3"
import asyncio

from whatsapie import Whatsapie, Text

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = Text(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())
```

`Whatsapie` and `Text` are two classes from our package that we're importing. The primary manager class is whatsapie, and you must use it to create a new manager. You can have several managers for your various WhatsApp businesses.

```py title="hello_world.py" linenums="1" hl_lines="5"
import asyncio

from whatsapie import Whatsapie, Text

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = Text(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())
```

Both `ACCESS_TOKEN` and `PHONE_NUMBER_ID` are now sent as parameters. Both of these parameters are required; it is recommended that you save them as environment variables and import them into the module using `#!python os.getenv()`

```py title="hello_world.py" linenums="1" hl_lines="7 8 9 10"
import asyncio

from whatsapie import Whatsapie, Text

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = Text(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())
```

Now we're going to make an instance of the `#! Text` class, which represents a text message api object. A `to` and `body` argument are required in a Text. Every message classe, regardless of its type, receives the `to` parameter.

```py title="hello_world.py" linenums="1" hl_lines="12 13 14 15"
import asyncio

from whatsapie import Whatsapie, Text

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = Text(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

async def main():
    await manager.send(text_message)

asyncio.run(main())
```

Finally, we use the whatsapie manager instance and await the `#!python Whatsapie.send()` method inside an async function, and run it using `#!python asyncio.run(main())`. This method, in the background, accesses the api endpoint and sends the data from the message class as a json object body.

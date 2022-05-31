whatsapie, The first wrapper for Meta's Whatsapp cloud API. Before you begin, you must first obtain the [ACCESS_TOKEN](#) and [PHONE_NUMBER_ID](#), which are given in the [Prerequisites](/whatsapie/#prerequisites).

!!! note "Using ENV variables for security"

    Using `os.getenv()`, load the environment variables ACCESS TOKEN and PHONE NUMBER ID into the module

Here's how to use whatsapie to send a short hello world message to a Whatsapp subscriber in 10 lines!!!!

```py title="hello_world.py" linenums="1"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

This is how simple it is to use whatsapie to send a hello world message. 🥳

## Closer Look!

Let's take a closer look at what's happening!

```py title="hello_world.py" linenums="1" hl_lines="1"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

`Whatsapie` and `TextMessage` are two classes from our package that we're importing. The primary manager class is whatsapie, and you must use it to create a new manager. You can have several managers for your various WhatsApp businesses.

```py title="hello_world.py" linenums="1" hl_lines="3"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

Both `ACCESS_TOKEN` and `PHONE_NUMBER_ID` are now sent as parameters. Both of these parameters are required; it is recommended that you save them as environment variables and import them into the module using `#!python os.getenv()`

```py title="hello_world.py" linenums="1" hl_lines="5 6 7 8"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

Now we're going to make an instance of the `#! TextMessage` class, which represents a text message api object. A `to` and `body` argument are required in a TextMessage. Every message classe, regardless of its type, receives the `to` parameter.

```py title="hello_world.py" linenums="1" hl_lines="10"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

Finally, we use the whatsapie manager instance to invoke the `#!python Whatsapie.send()` method. This method, in the background, accesses the api endpoint and sends the data from the message class as a json object body.

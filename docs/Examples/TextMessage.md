## Basic Text Message

```py title="hello_world.py" linenums="1"
from whatsapie import Whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world"
)

manager.send(text_message)

```

## Basic Text Message with url preview

```py title="hello_world.py" linenums="1"
from whatsapie import whatsapie, TextMessage

manager = Whatsapie(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX",
    body="Hello world, https://helloworld.com",
    preview_url=True
)

manager.send(text_message)

```

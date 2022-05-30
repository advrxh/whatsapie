Whatsappy is the first wrapper for Meta's whatsapp cloud api.
Before starting you have to follow the only step listed in the [Prerequisites](/whatsappy/#prerequisites),
which is to obtain the [ACCESS_TOKEN](#) and [PHONE_NUMBER_ID](#)

!!! note "Using ENV variables for security"

    Store the ACCESS_TOKEN and PHONE_NUMBER_ID as environment variables and load it into the module using `os.getenv()`

Here's how to send a quick hello world to a whatsapp user using [whatsappy](/) in 10 lines!!!!.

```py title="hello_world.py" linenums="1"
from whatsappy import Whatsappy, TextMessage

manager = Whatsappy(ACCESS_TOKEN, PHONE_NUMBER_ID)

text_message = TextMessage(
    to="1XXXXXXXXX", # recipients registered whatsapp number
    body="Hello world"
)

manager.send(text_message)

```

That's how easy it's to send a hello world message using Whatsappy 🎇

# Whatsapy

Unofficial Wrapper for Meta's [Whatsap Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) written in python

## INSTALL

```bash
$ pip install whatsapy
```

## PREREQUISITES

-   Follow Meta's [Whatsapp Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api) and obtain, meta business app [ACCESS_TOKEN](#) and [PHONE_NUMBER_ID]()

*   For added security, store both of these values as environment variables

## Simple Hello World Text Message

```py
import os

from whatsapy import Whatsapy
from whatsapy import Message, Text

ACCESS_TOKEN = os.environ('ACCESS_TOKEN')
PHONE_NUMBER_ID = os.environ('PHONE_NUMBER_ID')

manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

message = Message(to="91XXXXXXXXXX") # use country code without +

text = Text("Hello world")

message.set_text(text)

manager.push(message)

```

## Docs

-   ### Text Messages

    ```py
    from Whatsapy import Text

    manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

    message = Message(to="91XXXXXXXXXX") # use country code without +

    text = Text(body="Hello world")

    message.set_text(text)

    manager.push(message)
    ```

-   ### Text Messages with link preview

    ```py
    from Whatsapy import Text

    manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

    message = Message(to="91XXXXXXXXXX") # use country code without +

    text = Text(body="Hello world", preview_url=True)

    message.set_text(text)

    manager.push(message)
    ```

-   ### Location messages

    **NOTE** Location and Text entities should be pushed in different message instances

    ```py
    from Whatsapy import Location

    manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

    location = Location(
        long="LONGITUDE",
        lat="LATITUDE",
        name="LOCATION_NAME",
        address="LOCATION_ADDRESS"
    )

    message.set_location(location)

    manager.push(message)
    ```

-   ### Media messages

    **NOTE** Currently supporting only media hosted in an external webserver. Media files and Text entities can be pushed in a single message.

    ```py
    from Whatsapy import Media

    manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

    media = Media(
        type="image", # supported types are image, video, document, audio
        link="https://cdn.example.com/image.png",
        caption="Image Caption", # captions are only supported with image entities
        # filename="file.png", filenames can only be changed with document entities
    )

    message.set_media(media)

    manager.push(message)
    ```

-   ### Medias can be sent before or after sending the text message entity accompanied in a Message instance.

    ```py
    from Whatsapy import Media

    manager = Whatsapy(ACCESS_TOKEN, PHONE_NUMBER_ID) # Create an API manager instance

    media = Media(
        type="image", # supported types are image, video, document, audio
        link="https://cdn.example.com/image.png",
        caption="Image Caption", # captions are only supported with image entities
        # filename="file.png", filenames can only be changed with document entities
    )

    message.set_media(media)
    message.set_media_order("after") # order can be either before or after
    manager.push(message)
    ```

# CONTRIBUTION

This repo is open for contribution, create an ISSUE/PR or volunteer for an existing ISSUE

Maintained by [Aadil Varsh](https://advrxh.github.io)

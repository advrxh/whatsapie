from typing import List

from whatsapie.ext.message.location import Location
from whatsapie.ext.message.media import Media
from whatsapie.ext.message.message import Message
from whatsapie.ext.message.text import Text


class Group:
    """Message Group

    Args:
        message_list: List of Messsage objects
    """

    def __init__(self, message_list: List[Text | Media | Location], to: str = None):
        self.message_list = message_list 
        self.to = to

        if self.to is not None:
            for i in range(0, len(self.message_list)):
               self.message_list[i].to = self.to

    def add_to_group(self, message: Message):
        
        if self.to is not None:
            message.to = self.to

        self.message_list.append(message)
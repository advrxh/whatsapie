from whatsapie.ext.message import Message

from whatsapie.constants import (
    CAPTION_ALLOWED_MEDIA_TYPES,
    FILENAME_ALLOWED_MEDIA_TYPES,
)


class MediaMessage(Message):
    """Inherits from Message class.

    Inherits from Message class, represents a Media Message api object.

    Args:
        type: Media type, Supports 'image', 'audio', 'document', 'video'
        link: Link to the hosted media on the web.
        caption: Media caption.
        filename: Media filename.
    """

    def __init__(
        self,
        to: str,
        type: str = None,
        link: str = None,
        caption: str = None,
        filename: str = None,
    ):

        self.set_params(type=type, link=link, caption=caption, filename=filename)
        super().__init__(to=to)

    def set_params(
        self, type: str, link: str, caption: str = None, filename: str = None
    ):
        """Sets the required instance parameters.

        Args:
            type: Media type, Supports 'image', 'audio', 'document', 'video'
            link: Link to the hosted media on the web.
            caption: Media caption.
            filename: Media filename.
        """
        self.type = type
        self.link = link
        self.caption = None
        self.filename = None

        if type in CAPTION_ALLOWED_MEDIA_TYPES:
            self.caption = caption

        if type in FILENAME_ALLOWED_MEDIA_TYPES:
            self.filename = filename

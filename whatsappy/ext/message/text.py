from whatsappy.ext.message import Message


class TextMessage(Message):
    """Inherits from Message class.

    Inherits from Message class, represents a Text Message api object.

    Args:
        body: Message body text.
        preview_url: Must be set to true, when you want to render the embed for the url in the body.
    """

    def __init__(
        self,
        to: str,
        body: str,
        preview_url: bool = False,
    ) -> None:
        self.body = body
        self.preview_url = preview_url

        super().__init__(to=to)

    def set_body(self, body: str):
        """Sets the body value.

        Args:
            body: Message body text.
        """
        self.body = body

    def preview_url(self, _state: bool = None):
        """Toggles the preview url state

        Args:
            _state: New preview_url state.
        """

        if _state is None:
            self.preview_url = not self.preview_url

        self.preview_url = _state

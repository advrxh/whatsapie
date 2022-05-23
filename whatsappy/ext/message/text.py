from whatsappy.ext.message import Message


class TextMessage(Message):
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
        self.body = body

    def set_preview_url(self, _state: bool = None):
        if _state is None:
            self.preview_url = not self.preview_url

        self.preview_url = _state

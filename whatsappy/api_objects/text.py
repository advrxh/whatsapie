class Text:
    """
    Whatsapy message Text object class
    """

    def __init__(self, body: str, preview_url: bool = False) -> None:
        self.body = body
        self.preview_url = preview_url

    def set_body(self, body: str):
        self.body = body

    def set_preview_url(self, _state: bool = None):
        if _state is None:
            self.preview_url = not self.preview_url

        self.preview_url = _state

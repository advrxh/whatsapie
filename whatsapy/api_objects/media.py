class Media:
    """
    Whatsapp message Media object class
    """

    def __init__(self, type: str, link: str, caption: str = None, filename: str = None):

        self.type = type
        self.link = link
        self.caption = None
        self.filename = None

        if type in ["document", "image"]:
            self.caption = caption

        if type == "document":
            self.filename = filename

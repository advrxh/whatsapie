class Parameter:
    """Individual parameter for a Template message Component.

    Args:
        type: Parameter type
    """

    def __init__(self, type: str = None) -> None:
        self.type = type


class TextParam(Parameter):

    """Inherits from Parameter class.

    Represents a Currency Parameter.

    Args:
        text: Parameter text
    """

    def __init__(self, text: str = None) -> None:
        self.text = text
        super().__init__(type="text")


class Currency(Parameter):
    """Inherits from Parameter class.

    Represents a Currency Parameter.

    Args:
        fallback_value: Default fallback value if localization fails
        code: ISO 4217 currency code
        amount_1000: Amount multiplied by 1000
    """

    def __init__(
        self, fallback_value: str = None, code: str = None, amount_1000: int = 0
    ) -> None:
        self.fallback_value = fallback_value
        self.code = code
        self.amount_1000 = amount_1000
        super().__init__(type="currency")


class DateTime(Parameter):
    """Inherits from Parameter class.

    Represents a Date_Time Parameter.

    Args:
        fallback_value: Default fallback value if localization fails
    """

    def __init__(self, fallback_value: str = None) -> None:
        self.fallback_value = fallback_value
        super().__init__(type="date_time")


class MediaParam(Parameter):
    """Inherits from Parameter class.

    Represents a Media Parameter


    Args:
        type: Media type, Supports 'image', 'audio', 'document', 'video'
        link: Link to the hosted media on the web.
        caption: Media caption.
        filename: Media filename.
    """

    def __init__(
        self,
        type: str = None,
        link: str = None,
        caption: str = None,
        filename: str = None,
    ) -> None:
        self.type = type
        self.link = link
        self.caption = caption
        self.filename = filename
        super().__init__(type=type)

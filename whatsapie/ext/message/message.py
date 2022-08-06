class Message:
    """Custom python Message class representing a message api object.

    Args:
        to: Phone number of the recipient, must not contain '+' prefix.
    """

    def __init__(self, to: str = None) -> None:
        self.to = to

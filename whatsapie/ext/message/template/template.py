from typing import List

from whatsapie.ext.message.message import Message
from whatsapie.ext.message.template.components import Component


class Template(Message):
    """Inherits from Message class

    Inherits from Message class, represents a Template Message

    Args:
        name: Template name
        language_code: Language code (supports language with locale). For eg: 'en' or 'en_US'
        components: A list of Component object
    """

    def __init__(
        self,
        to: str = None,
        name: str = None,
        language_code: str = "en_US",
        components: List[Component] = [],
    ) -> None:
        self.name = name
        self.language_code = language_code
        self.components = components
        super().__init__(to=to)

    def add_component(self, component: Component):
        """Adds new component to existing list of components.

        Args:
            component: Component object
        """
        self.components.append(component)

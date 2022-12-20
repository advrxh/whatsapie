from typing import List

from whatsapie.ext.message.template.parameters import Parameter


class Component:
    """Individual component from a Template Message.

    Args:
        type: Component type
        parameters: List of Parameter object for the component
    """

    def __init__(self, type: str = None, parameters: List[Parameter] = []) -> None:
        self.type = type
        self.parameters = parameters

    def add_parameter(self, parameter: Parameter):
        self.parameters.append(parameter)


class Header(Component):
    """Inherits from Component Class.

    Represents a header component

    Args:
        parameters: List of Parameter object for the component
    """

    def __init__(self, parameters: List[Parameter] = []) -> None:
        super().__init__(type="header", parameters=parameters)


class Body(Component):
    """Inherits from Component Class.

    Represents a header component

    Args:
        parameters: List of Parameter object for the component
    """

    def __init__(self, parameters: List[Parameter] = []) -> None:
        super().__init__(type="body", parameters=parameters)

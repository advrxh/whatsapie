from whatsapie.constants import (
    CAPTION_ALLOWED_MEDIA_TYPES,
    FILENAME_ALLOWED_MEDIA_TYPES,
)
from whatsapie.ext.message import Template
from whatsapie.ext.message.template.components import *
from whatsapie.ext.message.template.parameters import *


def _generate_parameter_schema(parameter: Parameter):
    _parameter_schema = {}

    _parameter_schema["type"] = parameter.type

    if isinstance(parameter, Currency):
        _parameter_schema[parameter.type] = {
            "fallback_value": parameter.fallback_value,
            "code": parameter.code,
            "amount_1000": parameter.amount_1000,
        }

    if isinstance(parameter, DateTime):
        _parameter_schema[parameter.type] = {"fallback_value": parameter.fallback_value}

    if isinstance(parameter, TextParam):
        _parameter_schema[parameter.type] = parameter.text

    if isinstance(parameter, MediaParam):
        _parameter_schema[parameter.type] = {"link": parameter.link}

        if (
            parameter.type in CAPTION_ALLOWED_MEDIA_TYPES
            and parameter.caption is not None
        ):
            _parameter_schema[parameter.type]["caption"] = parameter.caption

        if (
            parameter.type in FILENAME_ALLOWED_MEDIA_TYPES
            and parameter.filename is not None
        ):
            _parameter_schema[parameter.type]["filename"] = parameter.filename

    return _parameter_schema


def _generate_component_schema(component: Component):
    _component_schema = {}

    _component_schema["type"] = component.type

    _component_schema["parameters"] = []

    for parameter in component.parameters:
        _component_schema["parameters"].append(_generate_parameter_schema(parameter))

    return _component_schema


def generate_template_schema(body: dict, message: Template):
    """Generate schema for Template

    Args:
        body: Parent api schema object.
        message: Template instance.

    Returns:
        body: Schema body
    """

    body["type"] = "template"
    body["template"] = {
        "name": message.name,
        "language": {"code": message.language_code},
    }

    body["template"]["components"] = []

    for component in message.components:
        body["template"]["components"].append(_generate_component_schema(component))

    return body

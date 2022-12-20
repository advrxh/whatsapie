class Address:
    """Address object

    Args:
        street: Optional. Street number and name.
        city: Optional. City name.
        state: Optional. State abbreviation.
        zip_code: Optional. ZIP code.
        country: Optional. Full country name.
        country_code: Optional. Two-letter country abbreviation.
        type: Optional. Standard values are HOME and WORK.
    """

    def __init__(
        self,
        street: str = None,
        city: str = None,
        state: str = None,
        zip_code: str = None,
        country: str = None,
        country_code: str = None,
        type: str = None,
    ) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.country_code = country_code
        self.type = type


class Email:
    """Email Object
    Args:
        email: Optional. Email address.
        type: Optional. Standard values are HOME and WORK.
    """

    def __init__(self, email: str = None, type: str = None) -> None:
        self.email = email
        self.type = type


class Name:
    """Name object
    Args:
        formatted_name: Required. Full name, as it normally appears.
        first_name: Optional*. First name.
        last_name: Optional*. Last name.
        middle_name: Optional*. Middle name.
        suffix: Optional*. Name suffix.
        prefix: Optional*. Name prefix.
    """

    def __init__(
        self,
        formatted_name: str,
        first_name: str = None,
        last_name: str = None,
        middle_name: str = None,
        suffix: str = None,
        prefix: str = None,
    ) -> None:
        self.formatted_name = formatted_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.suffix = suffix
        self.prefix = prefix


class Organization:
    """Organization object

    Args:
        company: Optional. Name of the contact's company.
        department: Optional. Name of the contact's department.
        title: Optional. Contact's business title.
    """

    def __init__(
        self, company: str = None, department: str = None, title: str = None
    ) -> None:
        self.company = company
        self.department = department
        self.title = title


class Phone:
    """Phone object

    Args:
        phone: Optional. Automatically populated with the `wa_id` value as a formatted phone number.
        type: Optional. Standard Values are CELL, MAIN, IPHONE, HOME, and WORK.
        wa_id: Optional. WhatsApp ID.
    """

    def __init__(self, phone: str = None, type: str = None, wa_id: str = None) -> None:
        self.phone = phone
        self.type = type
        self.wa_id = wa_id


class Url:
    """Url object

    Args:
        url: Optional. URL.
        type: Optional. Standard values are HOME and WORK.
    """

    def __init__(self, url: str = None, type: str = None) -> None:
        self.url = url
        self.type = type

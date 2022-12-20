from typing import List

from whatsapie.ext.message import ContactGroup
from whatsapie.ext.message.contact import *


def _generate_addresses_schema(addresses: List[Address]):
    _address_schema = []

    for address in addresses:
        _address_schema.append(
            {
                "street": address.street if address.street is not None else "None",
                "city": address.city if address.city is not None else "None",
                "state": address.state if address.state is not None else "None",
                "zip": address.zip_code if address.zip_code is not None else "None",
                "country": address.country if address.country is not None else "None",
                "country_code": address.country_code
                if address.country_code is not None
                else "None",
                "type": address.type if address.type is not None else "HOME",
            }
        )

    return _address_schema


def _generate_emails_schema(emails: List[Email]):
    _emails_schema = []

    for email in emails:
        _emails_schema.append(
            {
                "email": email.email,
                "type": email.type if email.type is not None else "PERSONAL",
            }
        )

    return _emails_schema


def _generate_name_schema(name: Name):
    return {
        "formatted_name": name.formatted_name,
        "first_name": name.first_name,
        "last_name": name.last_name,
        "middle_name": name.middle_name,
        "suffix": name.suffix,
        "prefix": name.prefix,
    }


def _generate_org_schema(org: Organization):
    return {"company": org.company, "department": org.department, "title": org.title}


def _generate_phones_schema(phones: List[Phone]):
    _phones_schema = []

    for phone in phones:
        _phones_schema.append(
            {
                "phone": phone.phone,
                "type": phone.type if phone.type is not None else "PHONE",
                "wa_id": phone.wa_id,
            }
        )

    return _phones_schema


def _generate_urls_schema(urls: List[Url]):

    _urls_schema = []

    for url in urls:
        _urls_schema.append({"url": url.url, "type": url.type})

    return _urls_schema


def _generate_contact_schema(contact: Contact):
    _contact_schema = {}

    _contact_schema["name"] = _generate_name_schema(contact.name)

    if len(contact.addresses) > 0:
        _contact_schema["addresses"] = _generate_addresses_schema(contact.addresses)

    if contact.birthday is not None:
        _contact_schema["birthday"] = contact.birthday

    if len(contact.emails) > 0:
        _contact_schema["emails"] = _generate_emails_schema(contact.emails)

    if contact.org is not None:
        _contact_schema["org"] = _generate_org_schema(contact.org)

    if len(contact.phones) > 0:
        _contact_schema["phones"] = _generate_phones_schema(contact.phones)

    if len(contact.urls) > 0:
        _contact_schema["urls"] = _generate_urls_schema(contact.urls)

    return _contact_schema


def generate_contact_group_schema(body: dict, message: ContactGroup):
    """Generate schema for ContactGroup.

    Args:
        body: Parent api schema object.
        message: ContactGroup instance.

    Returns:
        body: Schema body
    """

    body["type"] = "contacts"
    body["contacts"] = []

    for contact in message.contacts:
        body["contacts"].append(_generate_contact_schema(contact))

    return body

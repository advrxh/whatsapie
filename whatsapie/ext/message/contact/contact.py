from typing import List

from whatsapie.ext.message.contact.extra import *
from whatsapie.ext.message.message import Message


class Contact:
    """Contact object
    Args:
        addresses: List[Addresses]
        birthday: Birthday YYYY-MM-DD format
        emails: List[Email]
        name: Name object
        org: Organization object
        phones: List[Phone]
        urls: List[Url]
    """

    def __init__(
        self,
        name: Name,
        addresses: List[Address] = [],
        birthday: str = None,
        emails: List[Email] = [],
        org: Organization = None,
        phones: List[Phone] = [],
        urls: List[Url] = [],
    ) -> None:
        self.addresses = addresses
        self.birthday = birthday
        self.emails = emails
        self.name = name
        self.org = org
        self.phones = phones
        self.urls = urls

    def add_address(self, address: Address):
        self.addresses.append(address)

    def set_birthday(self, birthday: str):
        self.birthday = birthday

    def add_emails(self, email: Email):
        self.emails.append(email)

    def set_name(self, name: Name):
        self.name = name

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def add_url(self, url: Url):
        self.urls.append(url)


class ContactGroup(Message):
    """Inherits from Message class

    Inherits from Message class, represents a Contacts object

    Args:
        contacts: List[Contact] a list of Contact object
    """

    def __init__(self, to: str = None, contacts: List[Contact] = []) -> None:
        self.contacts = contacts
        super().__init__(to)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

from dataclasses import dataclass, field

from source.domain.email_address import EmailAddress
from source.ports.unsubscribed_email_address_repository import UnsubscribedEmailAddressRepository


@dataclass
class FakeUnsubscribedEmailAddressRepository(UnsubscribedEmailAddressRepository):
    index: set[EmailAddress] = field(default_factory=set)

    async def add(self, email_address: EmailAddress) -> None:
        self.index.add(email_address.value)

    async def is_unsubcribed(self, email_address: EmailAddress) -> bool:
        return email_address.value in self.index

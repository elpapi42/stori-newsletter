from dataclasses import dataclass
from uuid import UUID

from source.domain.email_address import EmailAddress
from source.ports.unsubscribed_email_address_repository import UnsubscribedEmailAddressRepository
from source.infrastructure.logger import Logger


@dataclass
class UnsubscribeEmailAddressService():
    unsubscribed_email_address_repo: UnsubscribedEmailAddressRepository

    async def execute(self, email: str) -> None:
        email_address = EmailAddress(value=email)

        await self.unsubscribed_email_address_repo.add(email_address)

        Logger.info("EmailAddressUnsubscribed", email_address=email_address.value)

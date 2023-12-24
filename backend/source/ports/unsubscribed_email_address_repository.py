from abc import ABC, abstractmethod

from source.domain.email_address import EmailAddress


class UnsubscribedEmailAddressRepository(ABC):
    @abstractmethod
    async def add(self, email_address: EmailAddress) -> None:
        raise NotImplementedError

    @abstractmethod
    async def is_unsubcribed(self, email_address: EmailAddress) -> bool:
        raise NotImplementedError

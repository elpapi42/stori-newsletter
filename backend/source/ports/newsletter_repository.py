from abc import ABC, abstractmethod
from uuid import UUID

from source.domain.newsletter import Newsletter


class NewsletterRepository(ABC):
    @abstractmethod
    async def add(self, newsletter: Newsletter) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: UUID) -> Newsletter:
        raise NotImplementedError

    @abstractmethod
    async def update(self, newsletter: Newsletter) -> None:
        raise NotImplementedError

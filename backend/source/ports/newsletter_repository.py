from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime

from source.domain.newsletter import Newsletter


class NewsletterRepository(ABC):
    @abstractmethod
    async def add(self, newsletter: Newsletter) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: UUID) -> Newsletter | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[Newsletter]:
        raise NotImplementedError

    @abstractmethod
    async def get_scheduled_for_timestamp(self, timestamp: datetime) -> list[Newsletter]:
        raise NotImplementedError

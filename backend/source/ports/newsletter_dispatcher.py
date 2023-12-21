from abc import ABC, abstractmethod

from source.domain.newsletter import Newsletter


class NewsletterDispatcher(ABC):
    @abstractmethod
    async def dispatch(self, newsletter: Newsletter) -> None:
        raise NotImplementedError

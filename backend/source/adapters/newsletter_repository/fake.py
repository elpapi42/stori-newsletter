from uuid import UUID

from source.ports.newsletter_repository import NewsletterRepository
from source.domain.newsletter import Newsletter


class FakeNewsletterRepository(NewsletterRepository):
    def __init__(self):
        self.index: dict[UUID, Newsletter] = {}

    async def add(self, newsletter: Newsletter) -> None:
        self.index[newsletter.id] = newsletter
        print(self.index)

    async def get(self, id: UUID) -> Newsletter:
        return self.index[id]

    async def update(self, newsletter: Newsletter) -> None:
        self.index[newsletter.id] = newsletter
        print(self.index)

from uuid import UUID

from source.ports.newsletter_repository import NewsletterRepository
from source.domain.newsletter import Newsletter


class FakeNewsletterRepository(NewsletterRepository):
    def __init__(self):
        self.index: dict[UUID, Newsletter] = {}

    async def add(self, newsletter: Newsletter) -> None:
        self.index[newsletter.id] = newsletter

    async def get(self, id: UUID) -> Newsletter | None:
        return self.index.get(id)

    async def get_all(self) -> list[Newsletter]:
        return list(self.index.values())

from dataclasses import dataclass
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.ports.newsletter_repository import NewsletterRepository
from source.infrastructure.logger import Logger


@dataclass
class GetAllNewslettersService():
    newsletter_repo: NewsletterRepository

    async def execute(self) -> list[Newsletter]:
        newsletters = await self.newsletter_repo.get_all()

        Logger.info(f"NewslettersFound", count=len(newsletters))

        return newsletters

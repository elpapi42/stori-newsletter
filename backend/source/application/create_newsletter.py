from dataclasses import dataclass
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.ports.newsletter_repository import NewsletterRepository
from source.infrastructure.logger import Logger


@dataclass
class CreateNewsletterService():
    newsletter_repo: NewsletterRepository

    async def execute(self, title: str) -> UUID:
        newsletter = Newsletter(title=title)

        await self.newsletter_repo.add(newsletter)

        Logger.info("NewsletterCreated", newsletter_id=str(newsletter.id))

        return newsletter.id

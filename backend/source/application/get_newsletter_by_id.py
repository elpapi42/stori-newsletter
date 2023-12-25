from dataclasses import dataclass
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.ports.newsletter_repository import NewsletterRepository
from source.infrastructure.logger import Logger


@dataclass
class GetNewsletterByIdService():
    newsletter_repo: NewsletterRepository

    async def execute(self, id: UUID) -> Newsletter | None:
        output = await self.newsletter_repo.get(id)

        if output is None:
            Logger.error("NewsletterNotFound", newsletter_id=str(id))
            return None

        Logger.info("NewsletterFound", newsletter_id=str(id))

        return output

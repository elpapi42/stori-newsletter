from dataclasses import dataclass
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.ports.newsletter_repository import NewsletterRepository
from source.ports.newsletter_dispatcher import NewsletterDispatcher


@dataclass
class SendNewsletterService():
    newsletter_repo: NewsletterRepository
    email_dispatcher: NewsletterDispatcher

    async def execute(self, id: UUID) -> None:
        newsletter = await self.newsletter_repo.get(id)

        await self.email_dispatcher.dispatch(newsletter)

from dataclasses import dataclass
from uuid import UUID

from source.domain.email_address import EmailAddress
from source.ports.newsletter_repository import NewsletterRepository


@dataclass
class UpdateNewsletterService():
    newsletter_repo: NewsletterRepository

    async def execute(self, id: UUID, audience: list[str], body: str) -> None:
        newsletter = await self.newsletter_repo.get(id)

        newsletter.audience = [EmailAddress(value=email) for email in audience]
        newsletter.body = body

        await self.newsletter_repo.update(newsletter)

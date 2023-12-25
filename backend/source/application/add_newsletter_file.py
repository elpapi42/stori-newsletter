from dataclasses import dataclass
from uuid import UUID
from io import IOBase

from source.ports.newsletter_repository import NewsletterRepository
from source.ports.file_storage import FileStorage
from source.infrastructure.logger import Logger
from source.application import exceptions


@dataclass
class AddNewsletterFileService():
    newsletter_repo: NewsletterRepository
    file_storage: FileStorage

    async def execute(self, newsletter_id: UUID, file: IOBase, ext: str) -> None:
        newsletter = await self.newsletter_repo.get(newsletter_id)
        if newsletter is None:
            Logger.error("AddingFileToNewsletterFailed", newsletter_id=str(newsletter_id))
            raise exceptions.NotFound(f"Newsletter with id {newsletter_id} not found")

        file_uri = await self.file_storage.save(str(newsletter.id), file, ext)

        newsletter.file_uri = file_uri

        await self.newsletter_repo.add(newsletter)

        Logger.info("NewsletterFileAdded", newsletter_id=str(newsletter_id))

from io import BytesIO

import pytest

from source.domain.newsletter import Newsletter
from source.application.add_newsletter_file import AddNewsletterFileService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository
from source.adapters.file_storage.fake import FakeFileStorage


@pytest.mark.asyncio
async def test_add_newsletter_file_service():
    fake_repo = FakeNewsletterRepository()
    fake_file_storage = FakeFileStorage()
    service = AddNewsletterFileService(fake_repo, fake_file_storage)

    newsletter = Newsletter(title="Original Title")

    await fake_repo.add(newsletter)

    await service.execute(
        newsletter_id=newsletter.id,
        file=BytesIO(b"Dummy file content"),
        ext="pdf"
    )

    updated_newsletter = await fake_repo.get(newsletter.id)

    assert updated_newsletter.file_uri == "/dummy/uri"

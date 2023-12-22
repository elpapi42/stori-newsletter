import pytest
from uuid import UUID

from source.application.create_newsletter import CreateNewsletterService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository


@pytest.mark.asyncio
async def test_create_newsletter_service():
    fake_repo = FakeNewsletterRepository()
    service = CreateNewsletterService(newsletter_repo=fake_repo)
    title = "Test Newsletter"

    result = await service.execute(title)

    assert isinstance(result, UUID)
    newsletter = await fake_repo.get(result)
    assert newsletter is not None
    assert newsletter.title == title

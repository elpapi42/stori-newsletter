import pytest
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.application.get_newsletter_by_id import GetNewsletterByIdService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository


@pytest.mark.asyncio
async def test_get_newsletter_by_id_service():
    fake_repo = FakeNewsletterRepository()
    service = GetNewsletterByIdService(newsletter_repo=fake_repo)

    newsletter = Newsletter(title="Original Title")

    await fake_repo.add(newsletter)

    newsletter = await service.execute(newsletter.id)

    assert newsletter is not None
    assert newsletter.title == "Original Title"

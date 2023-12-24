import pytest
from uuid import UUID

from source.domain.newsletter import Newsletter
from source.application.get_all_newsletters import GetAllNewslettersService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository


@pytest.mark.asyncio
async def test_get_all_newsletters_service():
    fake_repo = FakeNewsletterRepository()
    service = GetAllNewslettersService(newsletter_repo=fake_repo)

    newsletter = Newsletter(title="Original Title")

    await fake_repo.add(newsletter)

    newsletters = await service.execute()

    assert len(newsletters) == 1
    assert newsletters[0].id == newsletter.id
    assert newsletters[0].title == newsletter.title

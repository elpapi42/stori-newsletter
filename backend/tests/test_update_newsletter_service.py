import pytest

from source.domain.newsletter import Newsletter
from source.application.update_newsletter import UpdateNewsletterService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository


@pytest.mark.asyncio
async def test_update_newsletter_service():
    fake_repo = FakeNewsletterRepository()
    service = UpdateNewsletterService(newsletter_repo=fake_repo)
    newsletter = Newsletter(title="Original Title")

    await fake_repo.add(newsletter)

    new_title = "New Title"

    await service.execute(
        id=newsletter.id,
        title=new_title,
        audience=[],
        body=""
    )

    updated_newsletter = await fake_repo.get(newsletter.id)
    assert updated_newsletter is not None
    assert updated_newsletter.title == new_title

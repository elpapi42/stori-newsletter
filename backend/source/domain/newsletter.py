from uuid import UUID, uuid4
from datetime import datetime, timezone

from pydantic import BaseModel, Field, ConfigDict

from source.domain.email_address import EmailAddress


class Newsletter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=1)
    audience: list[EmailAddress] = []
    body: str = ""
    file_uri: str | None = None
    file_name: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = ConfigDict(validate_assignment=True)

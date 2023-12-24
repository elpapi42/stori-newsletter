from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict

from source.domain.email_address import EmailAddress


class Newsletter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=1)
    audience: list[EmailAddress] = []
    body: str = ""
    file_uri: str | None = None

    model_config = ConfigDict(validate_assignment=True)

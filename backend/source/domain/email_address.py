from pydantic import BaseModel, EmailStr


class EmailAddress(BaseModel):
    value: EmailStr

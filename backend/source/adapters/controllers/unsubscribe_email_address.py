from fastapi import APIRouter, Response
from pydantic import BaseModel, EmailStr

from source.application.unsubscribe_email_address import UnsubscribeEmailAddressService
from source.adapters.unsubscribed_email_address_repository.mongo import MongoUnsubscribedEmailAddressRepository


router = APIRouter()


class UnsubscribeEmailAdressInputDTO(BaseModel):
    email: EmailStr


@router.post("/unsubscribed-email-address", status_code=201)
async def unsubscribe_email_address(data: UnsubscribeEmailAdressInputDTO):
    unsubscribed_email_address_repo = MongoUnsubscribedEmailAddressRepository()
    unsubscribe_email_address_service = UnsubscribeEmailAddressService(unsubscribed_email_address_repo)

    await unsubscribe_email_address_service.execute(data.email)

    return Response(status_code=201)

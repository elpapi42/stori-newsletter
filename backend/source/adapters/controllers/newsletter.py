from uuid import UUID

from fastapi import APIRouter, Response, UploadFile, HTTPException
from pydantic import BaseModel, EmailStr

from source.application.create_newsletter import CreateNewsletterService
from source.application.update_newsletter import UpdateNewsletterService
from source.application.add_newsletter_file import AddNewsletterFileService
from source.application.send_newsletter import SendNewsletterService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository
from source.adapters.file_storage.local import LocalFileStorage
from source.adapters.newsletter_dispatcher.fake import FakeNewsletterDispatcher
from source.application import exceptions


router = APIRouter()


newsletter_repo = FakeNewsletterRepository()


class CreateNewsletterInputDTO(BaseModel):
    title: str


class CreateNewsletterOutputDTO(BaseModel):
    id: str


@router.post("/newsletter", response_model=CreateNewsletterOutputDTO, status_code=201)
async def create_newsletter(data: CreateNewsletterInputDTO):
    create_newsletter_service = CreateNewsletterService(newsletter_repo)

    newsletter_id = await create_newsletter_service.execute(data.title)

    return CreateNewsletterOutputDTO(id=str(newsletter_id))



class UpdateNewsletterInputDTO(BaseModel):
    title: str
    audience: list[EmailStr]
    body: str


@router.patch("/newsletter/{newsletter_id}", status_code=204)
async def update_newsletter(data: UpdateNewsletterInputDTO, newsletter_id: UUID):
    update_newsletter_service = UpdateNewsletterService(newsletter_repo)

    try:
        await update_newsletter_service.execute(
            id=newsletter_id,
            title=data.title,
            audience=data.audience,
            body=data.body
        )
    except exceptions.NotFound:
        raise HTTPException(404, detail="Newsletter not found")

    return Response(status_code=204)



mime_ext_mapping = {
    "image/jpeg": "jpg",
    "image/png": "png",
    "application/pdf": "pdf",
}


@router.post("/newsletter/{newsletter_id}/file", status_code=204)
async def create_newsletter_file(file: UploadFile, newsletter_id: UUID):
    file_storage = LocalFileStorage()
    add_newsletter_file_service = AddNewsletterFileService(newsletter_repo, file_storage)

    file_ext = mime_ext_mapping.get(file.content_type)
    if not file_ext:
        raise HTTPException(400, detail="Invalid file type")

    try:
        await add_newsletter_file_service.execute(
            newsletter_id=newsletter_id,
            file=file.file,
            ext=file_ext
        )
    except exceptions.NotFound:
        raise HTTPException(404, detail="Newsletter not found")

    return Response(status_code=204)



@router.post("/newsletter/{newsletter_id}/send", status_code=204)
async def send_newsletter(newsletter_id: UUID):
    newsletter_dispatcher = FakeNewsletterDispatcher()
    send_newsletter_service = SendNewsletterService(newsletter_repo, newsletter_dispatcher)

    try:
        await send_newsletter_service.execute(id=newsletter_id)
    except exceptions.NotFound:
        raise HTTPException(404, detail="Newsletter not found")

    return Response(status_code=204)

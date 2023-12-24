from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, Response, UploadFile, HTTPException
from pydantic import BaseModel, EmailStr, Field

from source.application.create_newsletter import CreateNewsletterService
from source.application.update_newsletter import UpdateNewsletterService
from source.application.add_newsletter_file import AddNewsletterFileService
from source.application.send_newsletter import SendNewsletterService
from source.application.get_all_newsletters import GetAllNewslettersService
from source.application.get_newsletter_by_id import GetNewsletterByIdService
from source.adapters.newsletter_repository.mongo import MongoNewsletterRepository
from source.adapters.file_storage.local import LocalFileStorage
from source.adapters.newsletter_dispatcher.ses import SESNewsletterDispatcher
from source.application import exceptions


router = APIRouter()


class CreateNewsletterInputDTO(BaseModel):
    title: str = Field(min_length=1)


class CreateNewsletterOutputDTO(BaseModel):
    id: str


@router.post("/newsletter", response_model=CreateNewsletterOutputDTO, status_code=201)
async def create_newsletter(data: CreateNewsletterInputDTO):
    newsletter_repo = MongoNewsletterRepository()
    create_newsletter_service = CreateNewsletterService(newsletter_repo)

    newsletter_id = await create_newsletter_service.execute(data.title)

    return CreateNewsletterOutputDTO(id=str(newsletter_id))



class UpdateNewsletterInputDTO(BaseModel):
    title: str
    audience: list[EmailStr]
    body: str
    file_name: str | None


@router.patch("/newsletter/{newsletter_id}", status_code=204)
async def update_newsletter(data: UpdateNewsletterInputDTO, newsletter_id: UUID):
    newsletter_repo = MongoNewsletterRepository()
    update_newsletter_service = UpdateNewsletterService(newsletter_repo)

    try:
        await update_newsletter_service.execute(
            id=newsletter_id,
            title=data.title,
            audience=data.audience,
            body=data.body,
            file_name=data.file_name,
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
    newsletter_repo = MongoNewsletterRepository()
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
    newsletter_repo = MongoNewsletterRepository()
    file_storage = LocalFileStorage()
    newsletter_dispatcher = SESNewsletterDispatcher(file_storage)
    send_newsletter_service = SendNewsletterService(newsletter_repo, newsletter_dispatcher)

    try:
        await send_newsletter_service.execute(id=newsletter_id)
    except exceptions.NotFound:
        raise HTTPException(404, detail="Newsletter not found")

    return Response(status_code=204)



class NewsletterDTO(BaseModel):
    id: UUID
    title: str
    audience: list[str]
    body: str
    file_name: str | None
    created_at: datetime



@router.get("/newsletter", status_code=200)
async def get_all_newsletters():
    newsletter_repo = MongoNewsletterRepository()
    get_all_newsletters_service = GetAllNewslettersService(newsletter_repo)

    newsletters = await get_all_newsletters_service.execute()

    return [
        NewsletterDTO(
            id=newsletter.id,
            title=newsletter.title,
            audience=[email.value for email in newsletter.audience],
            body=newsletter.body,
            file_name=newsletter.file_name,
            created_at=newsletter.created_at,
        )
        for newsletter in newsletters
    ]



@router.get("/newsletter/{newsletter_id}", status_code=200)
async def get_newsletter_by_id(newsletter_id: UUID):
    newsletter_repo = MongoNewsletterRepository()
    get_newsletter_by_id_service = GetNewsletterByIdService(newsletter_repo)

    newsletter = await get_newsletter_by_id_service.execute(newsletter_id)
    if not newsletter:
        raise HTTPException(404, detail="Newsletter not found")

    return NewsletterDTO(
        id=newsletter.id,
        title=newsletter.title,
        audience=[email.value for email in newsletter.audience],
        body=newsletter.body,
        file_name=newsletter.file_name,
        created_at=newsletter.created_at,
    )

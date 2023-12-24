from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    local_storage_path: str
    mongo_url: str
    sendgrid_api_key: str


default = Settings(_env_file='.env')

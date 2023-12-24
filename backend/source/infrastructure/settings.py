from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    local_storage_path: str
    mongo_url: str
    aws_access_key: str
    aws_secret_access_key: str


default = Settings(_env_file='.env')

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    local_storage_path: str
    mongo_url: str


default = Settings(_env_file='.env')

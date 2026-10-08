from pydantic import BaseSettings



class Settings(BaseSettings):
    path : int
    database_password : str = "localhost"
    database_username : str = "postgress"
    secret_key : str = "234ui34535435435"


settings = Settings()
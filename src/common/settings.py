from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    user_postgres: str
    host_postgres: str
    passw_postgres: str
    port_postgres: int = 5432
    db_postgres: str
    host_rabbit: str
    user_rabbit: str
    passw_rabbit: str
    port_rabbit: int = 5672
    queue: str = 'ofred_log'

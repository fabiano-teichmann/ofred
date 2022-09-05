import os


class Settings:
    def __init__(self):
        self.secret_key = os.environ.get('SECRET_KEY')
        self.host_postgres = os.environ.get('HOST_POSTGRES')
        self.user_postgres = os.environ.get('USER_POSTGRES')
        self.passw_postgres = os.environ.get('PASSW_POSTGRES')
        self.db_postgres = os.environ.get('DB_POSTGRES')
        self._validate_settings()

    def _validate_settings(self):
        if self.secret_key is None:
            raise ValueError('Error: SECRET_KEY not defined')
        if self.host_postgres is None:
            raise ValueError('Error: HOST_POSTGRES not defined')
        if self.user_postgres is None:
            raise ValueError('Error: USER_POSTGRES not defined')
        if self.passw_postgres is None:
            raise ValueError('Error: PASSW_POSTGRES not defined')
        if self.db_postgres is None:
            raise ValueError('Error: DB_POSTGRES not defined')

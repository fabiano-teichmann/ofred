import os


class Settings:
    def __init__(self):
        self.secret_key = os.environ.get('SECRET_KEY')
        self.host_postgres = os.environ.get('HOST_POSTGRES')
        self.user_postgres = os.environ.get('USER_POSTGRES')
        self.passw_postgres = os.environ.get('PASSW_POSTGRES')
        self.db_postgres = os.environ.get('DB_POSTGRES')
        self.host_rabbit = os.environ.get('HOST_RABBITMQ')
        self.user_rabbit = os.environ.get('USER_RABBITMQ')
        self.passw_rabbit = os.environ.get('PASSW_RABBITMQ')
        self.port_rabbit = os.environ.get('PORT_RABBITMQ', 5672)
        self.queue = 'ofred_log'
        self._validate_settings()

    def _validate_settings(self):
        if self.secret_key is None:
            raise ValueError('Error:Environ SECRET_KEY not defined')
        if self.host_postgres is None:
            raise ValueError('Error:Environ HOST_POSTGRES not defined')
        if self.user_postgres is None:
            raise ValueError('Error:Environ USER_POSTGRES not defined')
        if self.passw_postgres is None:
            raise ValueError('Error:Environ PASSW_POSTGRES not defined')
        if self.db_postgres is None:
            raise ValueError('Error:Environ DB_POSTGRES not defined')

        if self.host_rabbit is None:
            raise ValueError('Error:Environ HOST_RABBITMQ not defined')
        if self.user_rabbit is None:
            raise ValueError('Error:Environ USER_RABBITMQ not defined')
        if self.passw_rabbit is None:
            raise ValueError('Error:Environ PASSW_RABBITMQ not defined')

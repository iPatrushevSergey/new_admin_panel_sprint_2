"""Module with application settings."""

import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Load .env file into the environment variables and get them."""

    model_config = SettingsConfigDict(env_file='../.env', extra='ignore')

    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_password: str = os.getenv('DB_PASSWORD')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    db_schemas: str = os.getenv('DB_SCHEMAS')
    sqlite_db_path: str = os.getenv('SQLITE_DB_PATH', 'sqlite_to_postgres/db.sqlite')

    @property
    def postgresql(self):
        """
        Get the data source name of the postgresql database.

        Returns:
            DSN (dict[str, str | int]): Postgresql data source name.
        """
        return {
            'dbname': self.db_name,
            'user': self.db_user,
            'password': self.db_password,
            'host': self.db_host,
            'port': self.db_port,
        }

    @property
    def sqlite3(self):
        """
        Get the data source name of the postgresql database.

        Returns:
            DSN (dict[str, str | int]): Postgresql data source name.
        """
        return {'database': self.sqlite_db_path}


settings = Settings()

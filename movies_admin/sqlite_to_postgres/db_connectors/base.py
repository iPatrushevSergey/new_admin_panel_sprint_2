"""Module for base connector."""

from sqlite3 import Connection

from psycopg2.extensions import connection


class BaseDatabaseConnector(object):
    """Base connector to the database."""

    def __init__(self, db_connection: Connection | connection) -> None:
        """
        Initialize connector object. Defines protected attribute.

        Args:
            db_connection (Connection | connection): Connection to the database.
        """
        self._connect = db_connection

    def connect(self):
        """Get connection.

        Returns:
            self._connect (Connection | connection)
        """
        return self._connect

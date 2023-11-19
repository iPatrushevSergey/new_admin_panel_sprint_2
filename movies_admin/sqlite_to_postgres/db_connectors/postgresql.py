"""Module for defining PostgreSQL connector."""

from contextlib import contextmanager
from dataclasses import astuple, fields

from psycopg2.extensions import cursor
from psycopg2.extras import DictCursor, register_uuid

from db_connectors.base import BaseDatabaseConnector


class PostgresLoader(BaseDatabaseConnector):
    """Define an interface for interacting with PostgreSQL database."""

    @contextmanager
    def connect(self, row=False):
        """Connect to the SQLIte3 database with row factory - Row.

        Return the connection to the database and close it at the end
        of the connection.

        Args:
            row (bool): Rows in the key - value format (default tuple).

        Yields:
            self._connect (_connection): Return the connection to the database
            with cursor factory - DictCursor.
        """
        if row:
            self._connect.cursor_factory = DictCursor
        try:
            yield self._connect
        finally:
            self._connect.close()

    def prepare_tables(
        self,
        schema: str,
        table: str,
        db_cursor: cursor,
    ):
        """
        Prepare a table for writing data.

        Args:
            schema (str): Database schema
            table (str): Database table
            db_cursor (cursor): Cursor for working with data in the database.
        """
        register_uuid()
        db_cursor.execute('TRUNCATE {0}.{1}'.format(schema, table))

    def load_data(
        self,
        schema: str,
        table: str,
        db_cursor: cursor,
        table_data: set,
    ) -> None:
        """
        Make a insert query to the database.

        Args:
            schema (str): Database schema
            table (str): Database table
            db_cursor (cursor): Cursor for working with data in the database
            table_data (set): A container containing an entry from a table.
        """
        if not table_data:
            return

        column_names = [field.name for field in fields(table_data[0])]
        col_count = ', '.join(['%s' for _ in range(len(column_names))])
        bind_values = ','.join(
            db_cursor.mogrify(
                '({0})'.format(col_count), astuple(row),
            ).decode('utf-8') for row in table_data
        )

        column = ', '.join(column_names)

        stmt = (
            'INSERT INTO {0}.{1} '.format(schema, table) +
            '({0}) VALUES {1} '.format(column, bind_values) +
            'ON CONFLICT (id) DO NOTHING'
        )
        db_cursor.execute(stmt)

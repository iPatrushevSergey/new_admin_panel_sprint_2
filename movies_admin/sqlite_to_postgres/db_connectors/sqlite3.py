"""Module for defining SQLite3 connector."""

import logging
import sqlite3
from contextlib import contextmanager

from db_connectors.base import BaseDatabaseConnector


class SQLiteExtractor(BaseDatabaseConnector):
    """Define an interface for interacting with SQLite3 database."""

    @contextmanager
    def connect(self, row=False):
        """Connect to the SQLIte3 database with row factory - Row.

        Return the connection to the database and close it at the end
        of the connection.

        Args:
            row (bool): Rows in the key - value format (default tuple).

        Yields:
            self._connect (Connection): Return the connection to the database
            with row factory - Row.
        """
        if row:
            self._connect.row_factory = sqlite3.Row
        try:
            yield self._connect
        finally:
            self._connect.close()

    def extract(
        self,
        table: str,
        db_cursor: sqlite3.Cursor,
    ) -> list[sqlite3.Row]:
        """
        Make a select query to the database.

        Args:
            table (str): Database table
            db_cursor (Cursor): SQLite3 connection cursor

        Yields:
            data (list[sqlite.Row]): A stack of table rows of 1000 records.
        """
        try:
            db_cursor.execute('SELECT * FROM {0};'.format(table))

        except Exception as exc:
            logging.error(
                msg='An error occurred while extracting data ' +
                    'from {0}'.format(table) +
                    'the table. Error: {0}'.format(exc),
            )

        while rows := db_cursor.fetchmany(size=1000):
            yield rows

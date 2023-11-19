"""A module for implementing various ETL operations."""

import logging
import sqlite3
from argparse import Namespace

from psycopg2.extensions import connection as _connection

from db_connectors.postgresql import PostgresLoader
from db_connectors.sqlite3 import SQLiteExtractor
from transform_data.schema_mapping import (
    schema_tables_dataclasses_mapping as mapping,
)
from transform_data.transform import Transform


class ETLOperation(object):
    """Perform ETL operation."""

    def __init__(
        self,
        from_connect: sqlite3.Connection,
        to_connect: _connection,
    ):
        """
        Initialize the object by ETL operation with two connections.

        Args:
            from_connect (Connection): Connection to sqlite3 database
            to_connect (_connection): Connection to postgresql database.
        """
        self.from_connect = from_connect
        self.to_connect = to_connect

    def from_sqlite3_to_postgresql(self, args: Namespace):
        """
        Extract from sqlite3, transform and upload to postgresql.

        Args:
            args (Namespace): Parsed data from the command line.
        """
        sqlite_extractor = SQLiteExtractor(self.from_connect)
        postgres_loader = PostgresLoader(self.to_connect)
        transform = Transform()

        with (
            sqlite_extractor.connect(row=True) as sqlite_connect,
            postgres_loader.connect(row=True) as pg_connect,
            pg_connect.cursor() as pg_cur,
        ):
            sqlite_cur = sqlite_connect.cursor()

            load_schema = args.load_schema

            if isinstance(args.extract_table, list):
                extract_tables = args.extract_table
            else:
                extract_tables = [args.extract_table]

            if isinstance(args.extract_table, list):
                load_tables = args.load_table
            else:
                load_tables = [args.load_table]

            for num_table, extract_table in enumerate(extract_tables):
                load_table = load_tables[num_table]
                try:
                    postgres_loader.prepare_tables(
                        load_schema, load_table, pg_cur,
                    )
                except Exception as prepare_exc:
                    logging.error(
                        msg='An error occurred while preparing ' +
                            'the {0}'.format(load_table) +
                            'table. Error: {0}'.format(prepare_exc),
                    )

                for batch in sqlite_extractor.extract(extract_table, sqlite_cur):
                    try:
                        transform_data = transform.from_sqlite_to_postgresql(
                            load_schema, load_table, batch, mapping,
                        )
                    except Exception as transform_exc:
                        logging.error(
                            msg='An error occurred when converting data ' +
                                'to the loaded {0}'.format(load_table) +
                                'table. Error: {0}'.format(transform_exc),
                        )
                    try:
                        postgres_loader.load_data(
                            load_schema,
                            load_table,
                            pg_cur,
                            transform_data,
                        )
                    except Exception as load_exc:
                        logging.error(
                            msg='An error occurred when loading data ' +
                                'into the {0}'.format(load_table) +
                                'table. Error: {0}'.format(load_exc),
                        )
            pg_connect.commit()

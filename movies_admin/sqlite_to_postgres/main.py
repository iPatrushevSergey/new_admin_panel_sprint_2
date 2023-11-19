"""The main module for working with ETL operations."""

import argparse
import logging
import sqlite3

import psycopg2

from core.config import settings
from etl_operations.operations import ETLOperation


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for performing ETL operations')
    parser.add_argument(
        '-from',
        '--from_the_database',
        default='sqlite3',
        choices=['sqlite3'],
        help='Source for data extraction',
    )
    parser.add_argument(
        '-to',
        '--to_the_database',
        default='postgresql',
        choices=['postgresql'],
        help='Data download source',
    )
    parser.add_argument(
        '-es', '--extract_schema', help='Name of the database schema to extract',
    )
    parser.add_argument(
        '-ls',
        '--load_schema',
        default='content',
        help='Name of the database schema to download',
    )
    parser.add_argument(
        '-et',
        '--extract_table',
        default=['film_work', 'genre', 'person', 'genre_film_work', 'person_film_work'],
        help='Name of the database table to extract',
    )
    parser.add_argument(
        '-lt',
        '--load_table',
        default=['film_work', 'genre', 'person', 'genre_film_work', 'person_film_work'],
        help='Name of the database table to download',
    )
    args = parser.parse_args()

    db_connections = {
        'sqlite3': sqlite3.connect,
        'postgresql': psycopg2.connect,
    }
    from_db = args.from_the_database
    to_db = args.to_the_database

    try:
        with (
            db_connections[from_db](**getattr(settings, from_db)) as from_conn,
            db_connections[to_db](**getattr(settings, to_db)) as to_conn,
        ):
            getattr(
                ETLOperation(from_connect=from_conn, to_connect=to_conn),
                'from_{0}_to_{1}'.format(from_db, to_db),
            )(args)

    except sqlite3.ProgrammingError:
        logging.info(
            msg='Its all good. Since sqlite3 does not implement context ' +
                'manager methods, the session was closed earlier in ' +
                'the user context manager',
        )

"""Module for data transformation."""

from dataclasses import dataclass


class Transform(object):
    """Transform data from one database format to another."""

    def from_sqlite_to_postgresql(
        self,
        schema: str,
        table: str,
        table_data: dict,
        mapping: dict[str, dict],
    ) -> type:
        """
        Transform data from sqlite3 format to postgresql.

        Args:
            schema (str): Database schema
            table (str): Database table
            table_data (dict): Raw data from SQLite
            mapping (dict): Schema - tables - dataclasses mapping.

        Returns:
            dataclass object (type): Dataclass object with fields
            for PostgreSQL table.
        """
        diff_fields = {
            'created_at': 'created',
            'updated_at': 'modified',
        }

        transform_objects = []

        for row in table_data:
            record: dict = dict(row)
            copy_record: dict = record.copy()

            for column in record:
                if column in diff_fields:
                    copy_record[diff_fields.get(column)] = copy_record.pop(column)

            data_container: dataclass = mapping[schema][table](**copy_record)
            transform_objects.append(data_container)

        return transform_objects

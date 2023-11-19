"""A module for dataclasses for working with database tables."""

from dataclasses import dataclass, field
from datetime import date

from data_classes.mixins import (
    CreatedDataClassMixin,
    FilmworkDataClassMixin,
    GenreDataClassMixin,
    ModifiedDataClassMixin,
    PersonDataClassMixin,
    UUIDDataClassMixin,
)


@dataclass(frozen=True, slots=True)
class FilmworkDataClass(
    UUIDDataClassMixin,
    CreatedDataClassMixin,
    ModifiedDataClassMixin,
):
    """Form a dataclass Filmwork object."""

    title: str = field(default='')
    description: str = field(default=None)
    creation_date: date = field(default=None)
    rating: float = field(default=None)
    type: str = field(default='movie')
    file_path: str = field(default=None)


@dataclass(frozen=True, slots=True)
class GenreDataClass(
    UUIDDataClassMixin,
    CreatedDataClassMixin,
    ModifiedDataClassMixin,
):
    """Form a dataclass Genre object."""

    name: str = field(default='')
    description: str = field(default=None)


@dataclass(frozen=True, slots=True)
class PersonDataClass(
    UUIDDataClassMixin,
    CreatedDataClassMixin,
    ModifiedDataClassMixin,
):
    """Form a dataclass Person object."""

    full_name: str = field(default='')


@dataclass(frozen=True, slots=True)
class GenreFilmworkDataClass(
    UUIDDataClassMixin,
    CreatedDataClassMixin,
    GenreDataClassMixin,
    FilmworkDataClassMixin,
):
    """Form a dataclass GenreFilmwork object."""


@dataclass(frozen=True, slots=True)
class PersonFilmworkDataClass(
    UUIDDataClassMixin,
    CreatedDataClassMixin,
    FilmworkDataClassMixin,
    PersonDataClassMixin,
):
    """Form a dataclass PersonFilmwork object."""

    role: str = field(default='')

    def __eq__(self, other):
        """
        Perform a comparison of objects for equality.

        Args:
            other (object): The object to be compared with.

        Returns:
            result (bool): True - equal, False - not equal.
        """
        return (
            self.film_work_id == other.film_work_id and
            self.person_id == other.person_id
        )

    def __hash__(self) -> int:
        """
        Return the hash.

        Returns:
            result (int): Hash calculated from object attributes.
        """
        return hash((self.film_work_id, self.person_id))

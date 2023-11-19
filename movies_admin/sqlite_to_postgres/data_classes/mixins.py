"""A module for mixins dataclasses."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class FilmworkDataClassMixin(object):
    """Filmwork dataclass mixin."""

    film_work_id: UUID


@dataclass(frozen=True)
class GenreDataClassMixin(object):
    """Genre dataclass mixin."""

    genre_id: UUID


@dataclass(frozen=True)
class PersonDataClassMixin(object):
    """Person dataclass mixin."""

    person_id: UUID


@dataclass(frozen=True)
class UUIDDataClassMixin(object):
    """UUID dataclass mixin."""

    id: UUID = field(default_factory=uuid4)


@dataclass(frozen=True)
class CreatedDataClassMixin(object):
    """Created dataclass mixin."""

    created: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class ModifiedDataClassMixin(object):
    """Modified dataclass mixin."""

    modified: datetime = field(default_factory=datetime.now)

"""Through models."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models.abstract_models import UUIDMixin


class RoleType(models.TextChoices):
    """Choosing the role of a person."""

    director = 'director'
    writer = 'writer'
    actor = 'actor'


class GenreFilmwork(UUIDMixin):
    """Bind models `Genre` and `Filmwork`."""

    film_work = models.ForeignKey(
        'Filmwork',
        on_delete=models.CASCADE,
        verbose_name=_('film_work'),
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        verbose_name=_('genre'),
    )
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta(object):
        """Settings for the `GenreFilmwork` table in the database."""

        db_table = 'content\".\"genre_film_work'
        constraints = (
            models.UniqueConstraint(
                fields=('film_work', 'genre'),
                name='unique_film_work_genre',
            ),
        )

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return (
            f'{self.__class__.__name__}({self.id}, {self.film_work}, ' +
            f'{self.genre}, {self.created})'
        )


class PersonFilmwork(UUIDMixin):
    """Bind models `Person` and `Filmwork`."""

    film_work = models.ForeignKey(
        'Filmwork',
        on_delete=models.CASCADE,
        verbose_name=_('film_work'),
    )
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        verbose_name=_('person'),
    )
    role = models.CharField(_('role'), choices=RoleType.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        """Settings for the `PersonFilmwork` table in the database."""

        db_table = 'content\".\"person_film_work'
        constraints = (
            models.UniqueConstraint(
                fields=('film_work', 'person', 'role'),
                name='unique_film_work_person_role',
            ),
        )

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return (
            f'{self.__class__.__name__}({self.id}, {self.film_work}, ' +
            f'{self.person}, {self.role}, {self.created})'
        )

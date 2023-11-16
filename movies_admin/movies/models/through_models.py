"""Through models."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models.abstract_models import UUIDMixin


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
                fields=('filmwork', 'genre'),
                name='unique_film_work_genre',
            ),
        )

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return '{0}({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__,
            self.id,
            self.film_work,
            self.genre,
            self.created,
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
    role = models.TextField(_('role'), null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        """Settings for the `PersonFilmwork` table in the database."""

        db_table = 'content\".\"person_film_work'
        constraints = (
            models.UniqueConstraint(
                fields=('filmwork', 'person', 'role'),
                name='unique_film_work_person_role',
            ),
        )

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return '{0}({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__,
            self.id,
            self.film_work,
            self.person,
            self.role,
            self.created,
        )

"""Filmwork model."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models.abstract_models import TimeStampedMixin, UUIDMixin
from movies.models.genre import Genre
from movies.models.person import Person

STR_LENGTH255 = 255


class FilmworkType(models.TextChoices):
    """Choosing the filmwork type."""

    movie = 'movie'
    tv_show = 'tv_show'


class Filmwork(UUIDMixin, TimeStampedMixin):
    """
    Describes the `Filmwork` table in the database, initializing objects.

    Attrs:
        title (str): Title of the filmwork
        description (str): Description of the filmwork
        creation_date (date): Creation of the filmwork
        rating (float): Rating of the filmwork
        type (str): Type of filmwork
        created (datetime): Date and time of creation of the filmwork
        modified (datetime): The last update of the filmwork.
    """

    title = models.CharField(_('title'), max_length=STR_LENGTH255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation date'), db_index=True)
    rating = models.FloatField(
        _('rating'),
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    type = models.CharField(_('type'), choices=FilmworkType.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    file_path = models.FileField(
        _('file'),
        blank=True,
        null=True,
        upload_to='movies/',
    )
    persons = models.ManyToManyField(Person, through='PersonFilmwork')

    class Meta(object):
        """Settings for the `Filmwork` table in the database."""

        db_table = 'content\".\"film_work'
        verbose_name = _('Filmwork')
        verbose_name_plural = _('Filmworks')

    def __str__(self) -> str:
        """Return object name.

        Returns:
            (str): Object title.
        """
        return self.title

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return (
            f'{self.__class__.__name__}({self.id}, {self.title}, ' +
            f'{self.description}, {self.creation_date}, {self.rating}, ' +
            f'{self.type}, {self.created}, {self.modified})'
        )

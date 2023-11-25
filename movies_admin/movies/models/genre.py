"""Genre model."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models.abstract_models import TimeStampedMixin, UUIDMixin

STR_LENGTH255 = 255


class Genre(UUIDMixin, TimeStampedMixin):
    """
    Describes the `Genre` table in the database, initializing objects.

    Attrs:
        id (uuid): Unique primary key
        name (str): Name of the filmwork genre
        description (str): Description of the filmwork genre
        created (datetime): Creation of the filmwork genre
        modified (datetime): The last update of the filmwork genre.
    """

    name = models.CharField(_('name'), unique=True, max_length=STR_LENGTH255)
    description = models.TextField(_('description'), blank=True)

    class Meta(object):
        """Settings for the `Genre` table in the database."""

        db_table = 'content\".\"genre'
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self) -> str:
        """Return object name.

        Returns:
            (str): Object name.
        """
        return self.name

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return (
            f'{self.__class__.__name__}({self.id}, {self.name}, ' +
            f'{self.description}, {self.created}, {self.modified})'
        )

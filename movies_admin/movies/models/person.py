"""Person model."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models.abstract_models import TimeStampedMixin, UUIDMixin

STR_LENGTH255 = 255


class Person(UUIDMixin, TimeStampedMixin):
    """
    Describes the `Person` table in the database, initializing objects.

    Attrs:
        id (uuid): Unique primary key
        full_name (str): Filmwork member full name
        created (datetime): Creation of the filmwork person
        modified (datetime): The last update of the filmwork person.
    """

    full_name = models.CharField(_('full_name'), max_length=STR_LENGTH255)

    class Meta(object):
        """Settings for the `Person` table in the database."""

        db_table = 'content\".\"person'
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self) -> str:
        """Return object name.

        Returns:
            (str): Object full_name.
        """
        return self.full_name

    def __repr__(self) -> str:
        """Return the name of the object during inspection.

        Returns:
            (str): All fields of the object.
        """
        return '{0}({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__,
            self.id,
            self.full_name,
            self.created,
            self.modified,
        )

"""Abstract models - mixins."""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    """Add a mixin with a UUID ID."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        """Set abstractness."""

        abstract = True


class TimeStampedMixin(models.Model):
    """Add a mixin with the datetime fields `created` and `modified`."""

    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta(object):
        """Set abstractness."""

        abstract = True

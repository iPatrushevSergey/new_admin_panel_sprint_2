"""Module for configuring the display of models in the admin panel."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from movies.models.filmwork import Filmwork
from movies.models.genre import Genre
from movies.models.person import Person
from movies.models.through_models import GenreFilmwork, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    """Tabular inline for insertion into Filmwork model."""

    model = GenreFilmwork
    verbose_name = _('filmwork genre')
    verbose_name_plural = _('filmwork genres')


class PersonFilmworkInline(admin.TabularInline):
    """Tabular inline for insertion into Filmwork model."""

    model = PersonFilmwork
    autocomplete_fields = ('person',)
    verbose_name = _('filmwork person')
    verbose_name_plural = _('filmwork persons')


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    """Defines the settings of the Filmwork model in the admin panel."""

    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    list_display = (
        'title', 'type', 'creation_date', 'rating', 'created', 'modified',
    )
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Defines the settings of the Genre model in the admin panel."""

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Defines the settings of the Person model in the admin panel."""

    list_display = ('full_name',)
    list_filter = ('full_name',)
    search_fields = ('full_name',)

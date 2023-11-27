"""API views for the movies app."""

from typing import Any

from django.contrib.postgres.aggregates import ArrayAgg
from django.db import models
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models.filmwork import Filmwork


class MoviesApiMixin(object):
    """The class is a mixin. Define `get_queryset` and `render_to_response` methods."""

    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        """
        Form a queryset.

        Returns:
            queryset (Filmwork.queryset()): Return queryset.
        """
        return Filmwork.objects.annotate(
            actors=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=models.Q(personfilmwork__role='actor'),
            ),
            directors=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=models.Q(personfilmwork__role='director'),
            ),
            writers=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=models.Q(personfilmwork__role='writer'),
            ),
        ).values(
            'id', 'title', 'description', 'creation_date',
            'rating', 'type', 'actors', 'directors', 'writers',
        ).annotate(
            genres=ArrayAgg('genres__name', distinct=True),
        )

    def render_to_response(self, context, **response_kwargs):
        """
        Render response.

        Args:
            context (dict): Response context
            response_kwargs (dict): Named response arguments.

        Returns:
            response (Response): Json response.
        """
        return JsonResponse(context)


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    """Class for processing get object by id."""

    pk_url_kwarg = 'id'

    def get_queryset(self):
        """
        Inherits `get_queryset` and extends it.

        Returns:
            filter_queryset (Filmwork.queryset()): Return queryset/
        """
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """
        Override the method `get_context_response`.

        Args:
            kwargs (dict): Named arguments.

        Returns:
            Filmwork (dict): Retrieves an object from a queryset.
        """
        return self.get_queryset().first()


class MoviesListApi(MoviesApiMixin, BaseListView):
    """Class for processing get all objects."""

    paginate_by = 50

    def get_context_data(self):
        """
        Override the method `get_context_data`.

        Returns:
            response (json): Paginated list of filmworks.
        """
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by,
        )

        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }

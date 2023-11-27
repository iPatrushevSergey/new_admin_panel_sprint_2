"""Urls for the movies app API."""

from django.urls import include, path

urlpatterns = [
    path('v1/', include('movies.api.v1.urls')),
]

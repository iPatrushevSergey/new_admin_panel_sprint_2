"""Table names to dataclasses mapping."""

from data_classes.table_classes import (
    FilmworkDataClass,
    GenreDataClass,
    GenreFilmworkDataClass,
    PersonDataClass,
    PersonFilmworkDataClass,
)

content_tables = {
    'film_work': FilmworkDataClass,
    'genre': GenreDataClass,
    'person': PersonDataClass,
    'genre_film_work': GenreFilmworkDataClass,
    'person_film_work': PersonFilmworkDataClass,
}

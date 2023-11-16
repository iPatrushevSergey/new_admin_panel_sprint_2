"""Generated by django 4.2.6 on 2023-10-23 19:49."""

import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Initializing migration.

    Create tables: Filmwork, Genre, Person, PersonFilmwork, GenreFilmwork.
    Add m2m fields to Filmwork: genres, persons.
    """

    str_length255 = 255

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ('created', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='created',
                )),
                ('modified', models.DateTimeField(
                    auto_now=True,
                    verbose_name='modified',
                )),
                ('title', models.CharField(
                    max_length=str_length255,
                    verbose_name='title',
                )),
                ('description', models.TextField(
                    blank=True,
                    verbose_name='description',
                )),
                ('creation_date', models.DateField(
                    verbose_name='creation date',
                )),
                ('rating', models.FloatField(
                    blank=True,
                    validators=[MinValueValidator(0), MaxValueValidator(100)],
                    verbose_name='rating',
                )),
                ('type', models.CharField(
                    choices=[('movie', 'Movie'), ('tv_show', 'Tv Show')],
                    verbose_name='type',
                )),
            ],
            options={
                'verbose_name': 'Filmwork',
                'verbose_name_plural': 'Filmworks',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ('created', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='created',
                )),
                ('modified', models.DateTimeField(
                    auto_now=True,
                    verbose_name='modified',
                )),
                ('name', models.CharField(
                    max_length=str_length255,
                    verbose_name='name',
                )),
                ('description', models.TextField(
                    blank=True,
                    verbose_name='description',
                )),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ('created', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='created',
                )),
                ('modified', models.DateTimeField(
                    auto_now=True,
                    verbose_name='modified',
                )),
                ('full_name', models.CharField(
                    max_length=str_length255,
                    verbose_name='full_name',
                )),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ('role', models.TextField(null=True, verbose_name='role')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='movies.filmwork',
                )),
                ('person', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='movies.person',
                )),
            ],
            options={
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ('created', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='created',
                )),
                ('film_work', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='movies.filmwork',
                )),
                ('genre', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='movies.genre',
                )),
            ],
            options={
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(
                through='movies.GenreFilmwork',
                to='movies.genre',
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(
                through='movies.PersonFilmwork',
                to='movies.person',
            ),
        ),
    ]

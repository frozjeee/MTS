from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtUpdatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Film(CreatedAtUpdatedAt):
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    release_date = models.DateField(verbose_name='Release Date')
    genres = models.ManyToManyField(
        'Genre',
        related_name='films',
        verbose_name='Genre'
    )
    director = models.ForeignKey(
        'Director',
        related_name='films',
        verbose_name='Director',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title


    class Meta:
        db_table = "film"
        verbose_name = _("Film")
        verbose_name_plural = _("Films")




class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name='Director name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "director"
        verbose_name = _("Director")
        verbose_name_plural = _("Director")


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Genre')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "genre"
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")


class Review(CreatedAtUpdatedAt):
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Review')
    rating = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
        verbose_name='Rating'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Author'
    )
    film = models.ForeignKey(
        'film',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Film'
    )

    def __str__(self):
        return f'{self.text:30}'


    class Meta:
        db_table = "review"
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

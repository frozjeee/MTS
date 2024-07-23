from django.contrib import admin
from .models import Film, Director, Genre, Review


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'director', 'display_genres', )
    list_filter = ('release_date', 'genres', 'director')
    search_fields = ('title', 'director__name', 'genre__name')
    ordering = ('title', )
    date_hierarchy = 'release_date'


    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    display_genres.short_description = 'Genres'


admin.site.register(Film, FilmAdmin)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Review)

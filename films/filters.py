import django_filters
from .models import Film


class FilmFilter(django_filters.FilterSet):
    rating = django_filters.RangeFilter()

    class Meta:
        model = Film
        fields = ['genres', 'rating']

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Film, Genre, Director, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'rating']


class FilmListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    director = DirectorSerializer(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'genres', 'description', 'director', 'release_date', 'rating']


class FilmDetailSerializer(FilmListSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Film
        fields = [
            'title',
            'description',
            'genres',
            'director',
            'release_date',
            'rating',
            'reviews',
        ]

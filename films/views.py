from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from film_library.permissions import IsAuthenticatedForWrite
from .filters import FilmFilter
from .models import Film, Review
from .serializers import FilmListSerializer, FilmDetailSerializer, ReviewSerializer


class FilmListView(ListCreateAPIView):
    """
    Show all films or create film.

    Items can be filtered by genre, rating,
    or can be ordered by release date.
    Release date is shown in a films list to see dates for filtering.
    """
    queryset = Film.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = (IsAuthenticatedForWrite, )
    filterset_class = FilmFilter
    ordering_fields = ['release_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(rating=Avg('reviews__rating', default=0))
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FilmListSerializer
        if self.request.method == 'POST':
            return FilmDetailSerializer     


class FilmDetailView(RetrieveUpdateDestroyAPIView):
    """
    Show/update/destroy film details including film reviews and ratings.
    """
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer
    permission_classes = (IsAuthenticatedForWrite, )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(rating=Avg('reviews__rating', default=0)) # Calculate average rating for selected film
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        genres = serializer.validated_data.pop('genres', None)
        instance = serializer.save()
        if genres is not None:
            instance.genres.set(genres)


class ReviewCreateView(CreateAPIView):
    """
    Create a new review with film rating.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        film_id = self.kwargs.get('pk')
        try:
            film = Film.objects.get(pk=film_id)
        except Film.DoesNotExist:
            return Response({"error": "Film not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already reviewed this film
        if Review.objects.filter(film=film, author=request.user).exists():
            return Response({"error": "You have already reviewed this film"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(film=film, author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

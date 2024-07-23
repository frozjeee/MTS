from django.urls import path
from .views import FilmListView, FilmDetailView, ReviewCreateView

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('films/<int:pk>/reviews/', ReviewCreateView.as_view(), name='review_create'),
]
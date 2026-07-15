from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("register/", views.register, name="register"),

    path("movies/", views.movie_list, name="movie_list"),

    path("movies/search/", views.search_movies, name="search_movies"),

    path("movies/sort/", views.sort_movies, name="sort_movies"),

    path("movies/filter/", views.filter_movies, name="filter_movies"),

    path(
        "movies/<int:movie_id>/",
        views.movie_detail,
        name="movie_detail"
    ),

    path(
        "movies/<int:movie_id>/review/",
        views.write_review,
        name="write_review"
    ),
]
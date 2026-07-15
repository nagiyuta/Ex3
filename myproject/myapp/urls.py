from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("movies/", views.movie_list, name="movie_list"),

    path(
        "movies/search/",
        views.movie_search,
        name="movie_search",
    ),

    path(
        "movies/<int:movie_id>/",
        views.movie_detail,
        name="movie_detail",
    ),

    path(
        "review/<int:movie_id>/",
        views.review,
        name="review",
    ),
]
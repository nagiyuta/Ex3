from django.http import HttpResponse


def home(request):
    return HttpResponse("Film Review Home")


def register(request):
    return HttpResponse("User Registration Page")


def movie_list(request):
    return HttpResponse("Movie List")


def search_movies(request):
    return HttpResponse("Search Movies")


def sort_movies(request):
    return HttpResponse("Sort Movies by Star Rating")


def filter_movies(request):
    return HttpResponse("Hide Movies Below Selected Rating")


def movie_detail(request, movie_id):
    return HttpResponse(f"Movie {movie_id}")


def write_review(request, movie_id):
    return HttpResponse(f"Write Review for Movie {movie_id}")
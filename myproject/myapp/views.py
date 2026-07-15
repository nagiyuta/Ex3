from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            return HttpResponse("Username is required.")

        if not password:
            return HttpResponse("Password is required.")

        if len(username) > 30:
            return HttpResponse("Username must be 30 characters or less.")

        if len(password) > 9:
            return HttpResponse("Password must be 9 characters or less.")

        return HttpResponse(f"Registered: {username}")
    
        return HttpResponse(
            f"Registered: {username}"
        )

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(
                username=username,
                password=password
            )
        except User.DoesNotExist:
            return HttpResponse("Invalid username or password.")

        request.session["user_id"] = user.id

        return HttpResponse(f"Welcome {user.username}")

    return render(request, "login.html")


def movie_list(request):
    keyword = request.GET.get("search", "")
    rating = request.GET.get("rating", "")

    return render(request, "movie_list.html")


def review(request, movie_id):
    if request.method == "POST":
        score = request.POST.get("rating")
        text = request.POST.get("review")
        
        if not score:
            return HttpResponse("Rating is required.")

        try:
            score = int(score)
        except ValueError:
            return HttpResponse("Rating must be a number.")

        if score < 0 or score > 10:
            return HttpResponse("Rating must be between 0 and 10.")

        if not text:
            return HttpResponse("Review cannot be empty.")

        return HttpResponse(
            f"Movie {movie_id}<br>"
            f"Rating={score}<br>"
            f"Review={text}"
        )

    return render(request, "review.html")
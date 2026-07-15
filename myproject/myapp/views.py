from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.db.models import Avg
from .models import User,Movie,Review

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
    search = request.GET.get("search", "").strip()
    rating = request.GET.get("rating", "").strip()

    movies = Movie.objects.annotate(
        average_rating=Avg("reviews__star_rating")
    ).order_by("title")

    if search:
        movies = movies.filter(title__icontains=search)

    if rating:
        try:
            minimum_rating = int(rating)

            if 0 <= minimum_rating <= 10:
                movies = movies.filter(
                    average_rating__gte=minimum_rating
                )
        except ValueError:
            pass

    context = {
        "movies": movies,
        "search": search,
        "rating": rating,
    }

    return render(request, "movie_list.html", context)


def movie_search(request):
    search = request.GET.get("search", "").strip()
    rating = request.GET.get("rating", "").strip()

    movies = Movie.objects.annotate(
        average_rating=Avg("reviews__star_rating")
    ).order_by("title")

    if search:
        movies = movies.filter(title__icontains=search)

    if rating:
        try:
            minimum_rating = int(rating)

            if 0 <= minimum_rating <= 10:
                movies = movies.filter(
                    average_rating__gte=minimum_rating
                )
        except ValueError:
            pass

    return render(
        request,
        "partials/movie_results.html",
        {"movies": movies},
    )

def movie_detail(request, movie_id):
    movie = get_object_or_404(
        Movie.objects.annotate(
            average_rating=Avg("reviews__star_rating")
        ),
        id=movie_id,
    )

    reviews = movie.reviews.select_related("user").all()

    context = {
        "movie": movie,
        "reviews": reviews,
    }

    return render(request, "movie_detail.html", context)

def review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        score = request.POST.get("rating", "").strip()
        text = request.POST.get("review", "").strip()

        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse(
                "You must log in before writing a review.",
                status=403,
            )

        if not score:
            return HttpResponse("Rating is required.", status=400)

        try:
            score = int(score)
        except ValueError:
            return HttpResponse(
                "Rating must be a number.",
                status=400,
            )

        if not 0 <= score <= 10:
            return HttpResponse(
                "Rating must be between 0 and 10.",
                status=400,
            )

        if not text:
            return HttpResponse(
                "Review text is required.",
                status=400,
            )

        user = get_object_or_404(User, id=user_id)

        Review.objects.create(
            user=user,
            movie=movie,
            star_rating=score,
            review_text=text,
        )

        return redirect("movie_detail", movie_id=movie.id)

    return render(
        request,
        "review.html",
        {"movie": movie},
    )
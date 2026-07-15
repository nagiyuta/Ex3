from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=9)

    def __str__(self):
        return self.username


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_image = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    star_rating = models.PositiveSmallIntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.movie.title} - {self.star_rating}/10"
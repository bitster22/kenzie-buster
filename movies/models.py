from django.db import models


class RatingMovie(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(
        max_length=20, choices=RatingMovie.choices, default=RatingMovie.G
    )
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies", null=True
    )
    orders = models.ManyToManyField(
        "users.User", related_name="movies_orders", through="movies_orders.MovieOrder"
    )

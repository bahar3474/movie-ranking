from django.db import models
from member.models import Member


class Movie(models.Model):
    title = models.CharField(max_length=255)
    suggester = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MovieScore(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()

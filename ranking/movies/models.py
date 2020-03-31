from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    suggester = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()

    def __str__(self):
        return self.title

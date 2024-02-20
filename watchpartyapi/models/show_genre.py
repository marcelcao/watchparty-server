from django.db import models

class ShowGenre(models.Model):
    genre = models.CharField(max_length=50)

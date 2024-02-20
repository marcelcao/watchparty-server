from django.db import models
from watchpartyapi.models import User, ShowGenre

class Show(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show_title = models.CharField(max_length=300)
    show_description = models.CharField(max_length=1000)
    show_poster = models.CharField(max_length=500)
    show_genre = models.ForeignKey(ShowGenre, on_delete=models.CASCADE)
    is_watching = models.BooleanField()

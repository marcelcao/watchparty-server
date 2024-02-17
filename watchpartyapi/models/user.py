from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    image_url = models.CharField(max_length=500)
    bio = models.CharField(max_length=1000)
    uid = models.CharField(max_length=500)

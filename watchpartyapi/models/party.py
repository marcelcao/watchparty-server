from django.db import models
from watchpartyapi.models import User, Show

class Party(models.Model):
    party_name = models.CharField(max_length=300)
    party_description = models.CharField(max_length=1000)
    discord_link = models.CharField(max_length=500)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()
    tv_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    
    @property
    def attended(self):
        return self.__attended

    @attended.setter
    def attended(self, value):
        self.__attended = value

from django.db import models
from watchpartyapi.models import User, Party

class PartyAttendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

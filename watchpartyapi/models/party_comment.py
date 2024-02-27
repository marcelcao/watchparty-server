from django.db import models
from .user import User
from .party import Party

class PartyComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    posted_on = models.DateField(auto_now_add=True)

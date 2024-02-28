from rest_framework import serializers
from watchpartyapi.models import Party, User, PartyComment

class PartySerializer(serializers.ModelSerializer):
  """JSON serializer for party comments"""
  class Meta:
    model = Party
    fields = ('id', 'author', 'party', 'comment', 'posted_on')
    depth = 1

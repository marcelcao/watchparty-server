from rest_framework import serializers
from watchpartyapi.models import Party

class PartySerializer(serializers.ModelSerializer):
  """JSON serializer for party attendees"""
  class Meta:
    model = Party
    fields = ('id', 'party_name', 'party_description', 'discord_link', 'organizer', 'date', 'time', 'tv_show', 'attended')
    depth = 1

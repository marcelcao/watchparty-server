from rest_framework import serializers
from watchpartyapi.models import PartyAttendee

class PartyAttendeeSerializer(serializers.ModelSerializer):
  """JSON serializer for party attendees"""
  class Meta:
    model = PartyAttendee
    fields = ('id', 'user', 'party')
    depth = 1

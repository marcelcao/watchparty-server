from rest_framework import serializers
from watchpartyapi.models import ShowGenre

class ShowGenreSerializer(serializers.ModelSerializer):
  """JSON serializer for show genre"""
  class Meta:
    model = ShowGenre
    fields = ('id', 'genre')
    depth = 0

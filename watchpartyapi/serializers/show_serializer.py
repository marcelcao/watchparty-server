from rest_framework import serializers
from watchpartyapi.models import Show

class ShowSerializer(serializers.ModelSerializer):
  """JSON serializer for tv shows"""
  class Meta:
    model = Show
    fields = ('id', 'user', 'show_title', 'sow_description', 'show_poster', 'show_genre', 'is_watching')
    depth = 1

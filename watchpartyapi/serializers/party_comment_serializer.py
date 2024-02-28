from rest_framework import serializers
from watchpartyapi.models import PartyComment

class PartyCommentSerializer(serializers.ModelSerializer):
  """JSON serializer for party comments"""
  class Meta:
    model = PartyComment
    fields = ('id', 'author', 'party', 'comment', 'posted_on')
    depth = 1

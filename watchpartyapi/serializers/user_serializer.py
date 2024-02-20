from rest_framework import serializers
from watchpartyapi.models import User

class UserSerializer(serializers.ModelSerializer):
  """JSON serializer for users"""
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'username', 'image_url', 'bio', 'uid')
    depth = 0

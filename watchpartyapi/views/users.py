"""View module for handling user requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import User
from watchpartyapi.serializers import UserSerializer

class UserView(ViewSet):
  """User View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single user"""
    
    try:
      user = User.objects.get(pk=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)
    except User.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all users in the database"""
    
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

  
  def update(self, request, pk):
    """Handles PUT request for user"""
    
    user = User.objects.get(pk=pk)
    uid = request.META["HTTP_AUTHORIZATION"]
    
    user.first_name = request.data["firstName"]
    user.last_name = request.data["lastName"]
    user.bio = request.data["bio"]
    user.image_url = request.data["imageUrl"]
    user.uid = uid
   
    user.save()
    serializer = UserSerializer(user)
    return Response (serializer.data, status=status.HTTP_200_OK)

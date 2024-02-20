"""View module for handling show genre requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from watchpartyapi.models import ShowGenre
from watchpartyapi.serializers import ShowGenreSerializer

class ShowGenreView(ViewSet):
  """Show Genre View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single show genre option"""
    
    try:
      show_genre = ShowGenre.objects.get(pk=pk)
      serializer = ShowGenreSerializer(show_genre)
      return Response(serializer.data)
    except ShowGenre.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all show genre options"""
    
    show_genre = ShowGenre.objects.all()
    serializer = ShowGenreSerializer(show_genre, many=True)
    return Response(serializer.data)

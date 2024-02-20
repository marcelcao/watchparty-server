"""View module for handling show requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import Show, ShowGenre, User
from watchpartyapi.serializers import ShowSerializer

class ShowView(ViewSet):

  """TV Show View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single show"""
    
    try:
      show = Show.objects.get(pk=pk)
      serializer = ShowSerializer(show)
      return Response(serializer.data)
    except Show.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all shows created by user"""
    
    show = Show.objects.all()
    user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    associated_user = show.filter(user=user)
    serializer = ShowSerializer(associated_user, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for shows"""
    show = Show.objects.get(pk=pk)
    show.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for show"""
    
    user = User.objects.get(uid=request.data["user"])
    show_genre = ShowGenre.objects.get(pk=request.data["showGenre"])
    is_watching = True
    
    show = Show.objects.create(
      user = user,
      show_title = request.data["showTitle"],
      show_description = request.data["showDescription"],
      show_poster = request.data["showPoster"],  
      show_genre = show_genre,
      is_watching = is_watching,
    )
    serializer = ShowSerializer(show)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for show"""
    
    show = Show.objects.get(pk=pk)
    
    show.show_title = request.data["showTitle"]
    show.show_description = request.data["showDescription"]
    show.show_poster = request.data["showPoster"]
    
    user = User.objects.get(uid=request.data["user"])
    show.user = user
    
    show_genre = ShowGenre.objects.get(pk=request.data["showGenre"])
    show.show_genre = show_genre
    
    is_watching = True
    show.is_watching = is_watching
    
    show.save()
    serializer = ShowSerializer(show)
    return Response (serializer.data, status=status.HTTP_200_OK)

  @action(methods=['PATCH'], detail=True)
  def watched(self, request, pk=None):
      """Custom action to mark a show as watched"""
      show = Show.objects.get(pk=pk)
      show.is_watching = False
      show.save()
      return Response({'status': 'TV show marked as watched'}, status=status.HTTP_200_OK)

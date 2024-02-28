"""View module for handling watch party comments requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from watchpartyapi.models import User, Party, PartyComment
from watchpartyapi.serializers import PartyCommentSerializer

class PartyCommentsView(ViewSet):

  """Watch Party Comments View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for party comments"""
    
    try:
      comment = PartyComment.objects.get(pk=pk)
      serializer = PartyCommentSerializer(comment)
      return Response (serializer.data)
    except PartyComment.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all party comments"""
    
    comments = PartyComment.objects.all()
    serializer = PartyCommentSerializer(comments, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for comment"""
    comment = PartyComment.objects.get(pk=pk)
    comment.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

  def update(self, request, pk):
    """Handle PUT requests for a comment in party"""
    party_comment = PartyComment.objects.get(pk=pk)
    party_comment.comment = request.data["comment"]
    party_comment.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

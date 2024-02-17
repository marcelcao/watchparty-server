"""View module for handling party attendee requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import PartyAttendee, Party, User
from watchpartyapi.serializers import PartyAttendeeSerializer

class PartyAttendeeView(ViewSet):
  """Party Attendee View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single party attendee"""
    
    try:
      party_attendee = PartyAttendee.objects.get(pk=pk)
      serializer = PartyAttendeeSerializer(party_attendee)
      return Response(serializer.data)
    except PartyAttendee.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all party attendees"""
    
    party_attendee = PartyAttendee.objects.all()
    serializer = PartyAttendeeSerializer(party_attendee, many=True)
    return Response(serializer.data)

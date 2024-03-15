"""View module for handling party attendee requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import PartyAttendee, Party, User
from watchpartyapi.serializers import PartyAttendeeSerializer, PartySerializer

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

  def destroy(self, request, pk):
    """Handles DELETE request for party attendee"""
    party_attendee = PartyAttendee.objects.get(pk=pk)
    party_attendee.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['get'], detail=False)
  def view_attended(self, request):
    """Method to get all the parties a user is attending"""
    
    uid = request.META['HTTP_AUTHORIZATION']
      
    if not uid:
        return Response({"error": "Authorization Error"}, status=status.HTTP_400_BAD_REQUEST)
      
    try:
        user = User.objects.get(uid=uid)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    attended = PartyAttendee.objects.filter(user=user)
    attended_parties_id = attended.values_list('party_id', flat=True)
    
    attended_parties = Party.objects.filter(pk__in=attended_parties_id)
    
    serializer = PartySerializer(attended_parties, many=True)
    return Response(serializer.data)

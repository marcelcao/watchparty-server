"""View module for handling watch party requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import User, Show, PartyAttendee, Party
from watchpartyapi.serializers import PartySerializer

class PartyView(ViewSet):

  """Watch Party View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for watch party"""
    
    try:
      party = Party.objects.get(pk=pk)
      serializer = PartySerializer(party)
      return Response(serializer.data)
    except Party.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all watch parties in database"""
    
    party = Party.objects.all()
    serializer = PartySerializer(party, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for order"""
    party = Party.objects.get(pk=pk)
    party.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for watch party"""
    
    organizer = User.objects.get(uid=request.data["organizer"])
    tv_show = Show.objects.get(pk=request.data["tvShow"])
    
    party = Show.objects.create(
      organizer = organizer,
      party_name = request.data["partyName"],
      discord_link = request.data["discordLink"],
      date = request.data["date"],  
      time = request.data["time"],
      tv_show = tv_show,
    )
    serializer = PartySerializer(party)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for party"""
    
    party = Party.objects.get(pk=pk)
    
    party.party_name = request.data["partyName"]
    party.party_description = request.data["partyDescription"]
    party.discord_link = request.data["discordLink"]
    
    organizer = User.objects.get(uid=request.data["organizer"])
    party.organizer = organizer
    
    tv_show = Show.objects.get(pk=request.data["tvShow"])
    party.tv_show = tv_show
    
    party.save()
    serializer = PartySerializer(party)
    return Response (serializer.data, status=status.HTTP_200_OK)

  @action(methods=['post'], detail=True)
  def attend(self, request, pk):
      """Post request for a user to attend a watch party"""

      user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
      party = Party.objects.get(pk=pk)
      PartyAttendee.objects.create(
          user=user,
          party=party
      )
      return Response({'message': 'Party Joined!'}, status=status.HTTP_201_CREATED)
      
  @action(methods=['delete'], detail=True)
  def leave(self, request, pk):
      """User Request to unjoin a watch party"""

      user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
      party = Party.objects.get(pk=pk)
      attendee = PartyAttendee.objects.get(
          user=user,
          party=party
      )
      attendee.delete()
      return Response({'message': 'You left the party'}, status=status.HTTP_204_NO_CONTENT)

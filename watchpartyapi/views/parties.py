"""View module for handling watch party requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from watchpartyapi.models import User, Show, PartyAttendee, Party, PartyComment
from watchpartyapi.serializers import PartySerializer, PartyAttendeeSerializer, PartyCommentSerializer

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
    
    parties = Party.objects.all()
    
    uid = request.META['HTTP_AUTHORIZATION']  
    user = User.objects.get(uid=uid)
      
    for party in parties:
      party.attended = len(PartyAttendee.objects.filter(
        user_id=user,
        party_id=party
      )) > 0
    
    serializer = PartySerializer(parties, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for party"""
    party = Party.objects.get(pk=pk)
    party.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for watch party"""
    
    organizer = User.objects.get(uid=request.data["organizer"])
    tv_show = Show.objects.get(pk=request.data["tvShow"])
    
    party = Party.objects.create(
      organizer = organizer,
      party_name = request.data["partyName"],
      party_description = request.data["partyDescription"],
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
    party.date = request.data["date"]
    party.time = request.data["time"]
    
    organizer = User.objects.get(uid=request.data["organizer"])
    party.organizer = organizer
    
    tv_show = Show.objects.get(pk=request.data["tvShow"])
    party.tv_show = tv_show
    
    party.save()
    serializer = PartySerializer(party)
    return Response (serializer.data, status=status.HTTP_200_OK)

    
  @action(methods=['get'], detail=True)
  def attendees(self, request, pk):
    """Method to get all the attendees in an associated party"""
    attendees = PartyAttendee.objects.all()
    associated_party = attendees.filter(party_id=pk)
    
    serializer = PartyAttendeeSerializer(associated_party, many=True)
    return Response(serializer.data)
  
  @action(methods=['post'], detail=True)
  def attend(self, request, pk):
    """Post request for user to attend watch party"""
    
    user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    party = Party.objects.get(pk=pk)
    party_attendee = PartyAttendee.objects.create(
      user=user,
      party=party
    )
    return Response({'message': 'Party Joined!'}, status=status.HTTP_201_CREATED)
  
  @action(methods=['delete'], detail=True)
  def leave(self, request, pk):
    """Delete request to leave a party"""
    
    user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    party = Party.objects.get(pk=pk)
    party_attendee = PartyAttendee.objects.get(
      user_id=user.id,
      party_id=party.id
    )
    party_attendee.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

  @action(methods=['post'], detail=True)
  def post_comment(self, request, pk):
    """Method to post a comment on a single party"""
    author = User.objects.get(uid=request.data["author"])
    party = Party.objects.get(pk=pk)
    party_comment = PartyComment.objects.create(
      author=author,
      party=party,
      comment=request.data["comment"]
    )
    return Response({'message': 'Comment posted!'}, status=status.HTTP_201_CREATED)
  
  @action(methods=['get'], detail=True)
  def view_comments(self, request, pk):
    """Method to get all the comments associated to a single party"""
    comments = PartyComment.objects.all()
    associated_party = comments.filter(party_id=pk)
    
    serializer = PartyCommentSerializer(associated_party, many=True)
    return Response(serializer.data)
  
  @action(methods=['get'], detail=False)
  def get_user_parties(self, request):
      """Method to get a user's parties for the profile page"""
      
      uid = request.META['HTTP_AUTHORIZATION']
      
      if not uid:
          return Response({"error": "Authorization Error"}, status=status.HTTP_400_BAD_REQUEST)
      
      try:
          user = User.objects.get(uid=uid)
      except User.DoesNotExist:
          return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
      

      parties = Party.objects.filter(organizer=user)
      
      for party in parties:
        party.attended = len(PartyAttendee.objects.filter(
          user_id=user,
          party_id=party
        )) > 0
      
          
      serializer = PartySerializer(parties, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

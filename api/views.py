from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response


# Create your views here.
class EventView(generics.ListAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class GetEventView(APIView):
  serializer_class = EventSerializer
  
  def get(self, request, format=None):
    
    if not request.user.is_authenticated:
      return Response({'Access Denied': f'User {request.user} must be authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    limit = request.GET.get('limit')
    if limit == None:
      data = [self.serializer_class(event).data for event in Event.objects.all()]
      return Response(data, status=status.HTTP_200_OK)
    if not limit.isdigit():
      return Response({'Bad request': 'Limit parameter must be integer'}, status=status.HTTP_400_BAD_REQUEST)
    data = list(self.serializer_class(event).data for event in Event.objects.all()[:int(limit)])
    return Response(data, status=status.HTTP_200_OK)
    


class CreateEventView(APIView):
  serializer_class = EventSerializer

  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if not(serializer.is_valid()):
      return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    name = serializer.data.get('name')
    date = serializer.data.get('date')
    ticket_price = serializer.data.get('ticket_price')
    address = serializer.data.get('address')
    likes = serializer.data.get('likes')

    event = Event(
      name=name,
      date=date,
      ticket_price=ticket_price,
      address=address,
      likes=likes
    )
    event.save()
    return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)

from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import EventSerializer, EventTagSerializer
from .models import Event, EventTag
from rest_framework.response import Response


# def auth_check(request):
#   if not request.user.is_authenticated:
#     return Response({'Access Denied': f'User must be authenticated'}, status=status.HTTP_403_FORBIDDEN)

# Create your views here.
class EventView(generics.ListAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class GetEventView(APIView):
  serializer_class = EventSerializer
  
  def get(self, request, format=None):
    if not request.user.is_authenticated:
      return Response({'Access Denied': f'User must be authenticated'}, status=status.HTTP_403_FORBIDDEN)

    limit = request.GET.get('_limit')
    page = request.GET.get('_page')

    data = [self.serializer_class(event).data for event in Event.objects.all()]
    if limit != None and limit.isdigit():
      if page == None or not page.isdigit():
        page = 1
      limit = int(limit)
      page = int(page)

      data = list(self.serializer_class(event).data for event in Event.objects.all()[limit*(page-1) : limit*page])

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


class GetRecommendEventView(APIView):

  def get(self, request, format=None):
    if not request.user.is_authenticated:
      return Response({'Access Denied': f'User must be authenticated'}, status=status.HTTP_403_FORBIDDEN)

    limit = request.GET.get('_limit')
    page = request.GET.get('_page')

    user_fav_tags = list(EventTagSerializer(tag).data['name'] for tag in request.user.fav_tags.all())
    user_liked_events = list(EventSerializer(event).data['name'] for event in request.user.liked_events.all())
    # return Response(user_liked_events, status=status.HTTP_200_OK)
    tag_coeff = {}
    all_tags = [EventTagSerializer(tag).data['name'] for tag in EventTag.objects.all()]

    for tag in all_tags:
      coeff = 0
      if tag in user_fav_tags:
        coeff += 10
      
      tag_coeff[tag] = coeff
    

    rec_dict = {}
    all_events = [EventSerializer(event).data for event in Event.objects.all()]
    for event in all_events:
      if event['name'] in user_liked_events:
        for tag in event['tags']:
          tag_coeff[tag['name']] += 0.1

    for event in all_events:
      total_coeff = 0
      for tag in event['tags']:
        total_coeff += tag_coeff[tag['name']]

      rec_dict[event['name']] = total_coeff

    rec_list_sorted = sorted(rec_dict, key=rec_dict.get, reverse=True)
    if limit != None and limit.isdigit():
      if page == None or not page.isdigit():
        page = 1
      limit = int(limit)
      page = int(page)
      
      rec_list_sorted = rec_list_sorted[limit*(page - 1) : limit*page]

    data = [EventSerializer(Event.objects.get(name=name)).data for name in rec_list_sorted]

    return Response(data, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Event  # Correct model name
from .serializers import EventSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Use Event model
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Use Event model
    event.delete()
    return Response({'message': 'Event deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_event_by_name(request, name):
    event = get_object_or_404(Event, name=name)  # Use Event model
    serializer = EventSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_event_by_code(request, code):
    event = get_object_or_404(Event, code=code)  # Use Event model
    serializer = EventSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_events(request):
    events = Event.objects.all()  # Use Event model
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def number_of_events(request):
    count = Event.objects.count()  # Use Event model
    return Response({'number_of_events': count}, status=status.HTTP_200_OK)

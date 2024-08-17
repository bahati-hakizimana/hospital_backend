from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Notification  # Correct model name
from .serializers import NotificationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_notification(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)  # Use notification model
    serializer = NotificationSerializer(notification, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)  # Use notification model
    notification.delete()
    return Response({'message': 'Notification deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_notification_by_name(request, name):
    notification = get_object_or_404(Notification, name=name)  # Use notification model
    serializer = NotificationSerializer(notification)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_notification_by_code(request, code):
    notification = get_object_or_404(Notification, code=code)  # Use notification model
    serializer = NotificationSerializer(notification)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_notifications(request):
    notifications = Notification.objects.all()  # Use notification model
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def number_of_notifications(request):
    count = Notification.objects.count()  # Use notification model
    return Response({'number_of_notifications': count}, status=status.HTTP_200_OK)


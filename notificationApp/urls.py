from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_notification, name='add_notificatio'),
    path('update/<int:notification_id>/', views.update_notification, name='update_notification'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('find/name/<str:name>/', views.find_notification_by_name, name='find_notification_by_name'),
    path('find/notification_code/<str:code>/', views.find_notification_by_code, name='find_notification_by_notification_code'),
    path('notifications/', views.display_notifications, name='display_notifications'),
    path('count/', views.number_of_notifications, name='number_of_notifications'),
]

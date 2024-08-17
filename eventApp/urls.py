from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_event, name='add_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('find/name/<str:name>/', views.find_event_by_name, name='find_event_by_name'),
    path('find/event_code/<str:code>/', views.find_event_by_code, name='find_event_by_event_code'),
    path('events/', views.display_events, name='display_events'),
    path('count/', views.number_of_events, name='number_of_events'),
]

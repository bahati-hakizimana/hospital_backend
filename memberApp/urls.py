# memberApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_member, name='create_member'),
    path('update/<int:member_id>/', views.update_member, name='update_member'),
    path('<int:member_id>/', views.get_member_by_id, name='get_member_by_id'),
    path('status/<str:status>/', views.get_members_by_status, name='get_members_by_status'),
    path('firstname/<str:firstname>/', views.get_members_by_firstname, name='get_members_by_firstname'),
    path('lastname/<str:lastname>/', views.get_members_by_lastname, name='get_members_by_lastname'),
    path('phone/<str:phone>/', views.get_member_by_phone, name='get_member_by_phone'),
]

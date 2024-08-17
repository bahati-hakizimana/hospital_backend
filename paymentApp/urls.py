# paymentApp/urls.py
from django.urls import path
from .views import make_payment, view_Payment

urlpatterns = [
    path('make_payment/', make_payment, name='make_payment'),
    path('payment/all/', view_Payment, name='payment_all'),
]

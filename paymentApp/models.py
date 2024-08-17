# paymentApp/models.py
# paymentApp/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Payment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10)
    reference = models.CharField(max_length=100)
    provider = models.CharField(max_length=50, blank=True, null=True)  # Add provider field
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.amount}'


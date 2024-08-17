# paymentApp/views.py
from decimal import Decimal
from django.http import JsonResponse
from paypack.client import HttpClient
from paypack.transactions import Transaction
from .models import Payment
from rest_framework.decorators import api_view
from rest_framework.response import Response

client_id = "22a6683c-3954-11ef-b91a-deade826d28d"
client_secret = "f4b599079c93c1d8088b2dda32536db0da39a3ee5e6b4b0d3255bfef95601890afd80709"

HttpClient(client_id=client_id, client_secret=client_secret)

@api_view(['POST'])
def make_payment(request):
    firstname = request.data.get('firstname')
    lastname = request.data.get('lastname')
    phone = request.data.get('phone')
    amount = request.data.get('amount')
    email = request.data.get('email')

    try:
        # Call the payment gateway to process the payment
        cashin = Transaction().cashin(amount=Decimal(amount), phone_number=phone)

        # Extract the necessary fields from the payment gateway response
        status = cashin.get('status', 'pending')
        reference = cashin.get('ref', '')
        provider = cashin.get('provider', '')  # Extract provider field

        print(provider)

        # Save payment details to the database with the correct status and provider
        Payment.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            phone_number=phone,
            amount=Decimal(amount),
            status=status,
            reference=reference,
            provider=provider  # Save the provider field
        )

        # Return the payment details including status and provider
        return JsonResponse(cashin, status=201)

    except Exception as e:
        # Return error details if something goes wrong
        return JsonResponse({'error': str(e)}, status=400)


from .serializers import PaymentSerializer

@api_view(['GET'])
def view_Payment(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response({'payments': serializer.data})

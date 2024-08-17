# memberApp/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from paypack.client import HttpClient
from paypack.transactions import Transaction
from .models import Member
from .serializers import MemberSerializer

# Initialize Paypack Client
client_id = "39c58eb4-3862-11ef-b0bf-deade826d28d"
client_secret = "4fab7c1f7bba3ff9b8203ecd6491e54bda39a3ee5e6b4b0d3255bfef95601890afd80709"
HttpClient(client_id=client_id, client_secret=client_secret)

@csrf_exempt
@api_view(['POST'])
def create_member(request):
    amount = request.data.get('amount')
    phone = request.data.get('phone')

    if not amount or not phone:
        return JsonResponse({'error': 'Amount and phone number are required'}, status=400)

    try:
        amount = float(amount)
    except ValueError:
        return JsonResponse({'error': 'Invalid amount'}, status=400)

    cashin = Transaction().cashin(amount=amount, phone_number=phone)
    print(f'\n\n Status: {cashin} \n\n')

    status = 'approved' if cashin.get('status') == 'success' else 'denied'

    member = Member.objects.create(
        firstname=request.data.get('firstname'),
        lastname=request.data.get('lastname'),
        phone=phone,
        user_id=request.data.get('user_id'),
        status=status
    )
    return JsonResponse({'id': member.id, 'status': member.status})

@csrf_exempt
@api_view(['POST'])
def update_member(request, member_id):
    if request.method == 'POST':
        member = get_object_or_404(Member, id=member_id)
        data = request.POST
        amount = data.get('amount')
        phone = data.get('phone')

        cashin = Transaction().cashin(amount=amount, phone_number=phone)

        member.status = 'approved' if cashin.get('status') == 'success' else 'denied'
        member.firstname = data.get('firstname', member.firstname)
        member.lastname = data.get('lastname', member.lastname)
        member.phone = phone
        member.user_id = data.get('user_id', member.user_id)
        member.save()

        return JsonResponse({'id': member.id, 'status': member.status})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@api_view(['GET'])
def get_member_by_id(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return JsonResponse({
        'id': member.id,
        'firstname': member.firstname,
        'lastname': member.lastname,
        'phone': member.phone,
        'status': member.status,
        'created_date': member.created_date,
    })

@api_view(['GET'])
def get_members_by_status(request, status):
    members = Member.objects.filter(status=status)
    data = [{'id': member.id, 'firstname': member.firstname, 'lastname': member.lastname, 'status': member.status} for member in members]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_members_by_firstname(request, firstname):
    members = Member.objects.filter(firstname__icontains=firstname)
    data = [{'id': member.id, 'firstname': member.firstname, 'lastname': member.lastname, 'status': member.status} for member in members]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_members_by_lastname(request, lastname):
    members = Member.objects.filter(lastname__icontains=lastname)
    data = [{'id': member.id, 'firstname': member.firstname, 'lastname': member.lastname, 'status': member.status} for member in members]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_member_by_phone(request, phone):
    member = get_object_or_404(Member, phone=phone)
    return JsonResponse({
        'id': member.id,
        'firstname': member.firstname,
        'lastname': member.lastname,
        'phone': member.phone,
        'status': member.status,
        'created_date': member.created_date,
    })

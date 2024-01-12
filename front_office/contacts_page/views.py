from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.utils import timezone


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact_message = Message(
            name=name, email=email, phone=phone, message=message)
        contact_message.save()

        response_data = {
            'success': True,
            'message': 'Message received! Thank you for contacting us.'
        }

        return JsonResponse(response_data)

    return render(request, 'contacts.html')

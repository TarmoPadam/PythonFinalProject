from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message
from .forms import MessageForm


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact_message = Message(
            name=name, email=email, phone=phone, message=message)
        contact_message.save()

        return render(request, 'contacts.html')

    return render(request, 'contacts.html')


def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)

    if request.method == 'GET':
        message.is_read = True
        message.save()

        return HttpResponseRedirect(reverse('admin:messages'))

    return render(request, 'message_detail.html', {'message': message})

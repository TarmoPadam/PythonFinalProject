from django.urls import path
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Message


@admin.register(Message)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message',
                    'created_at', 'view_message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

    def view_message(self, obj):
        url = reverse('admin:contacts_page_message_view_message',
                      args=[str(obj.id)])
        return format_html('<a href="{url}">View</a>', url=url)

    view_message.short_description = 'View'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('message_detail/<int:message_id>/', self.admin_site.admin_view(self.message_detail),
                 name='contacts_page_message_view_message'),
        ]
        return custom_urls + urls

    def message_detail(self, request, message_id):
        message = get_object_or_404(Message, pk=message_id)

        if request.method == 'POST':
            # Save the message to the database
            message.save()

            # Mark the message as read
            message.is_read = True
            message.save()

            # Redirect to the admin messages list
            return HttpResponseRedirect(reverse('admin:contacts_page_message'))

        # Display the message in the template
        return render(request, 'admin/contacts_page/message/message_detail.html', {'message': message})

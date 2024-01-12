from django.contrib import admin
from .models import Message


@admin.register(Message)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

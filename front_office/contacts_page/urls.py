from django.urls import path
from .views import contact_view, message_detail

urlpatterns = [
    path('', contact_view, name='contact_view'),
    path('message/<int:message_id>/',
         message_detail, name='view_message'),
]

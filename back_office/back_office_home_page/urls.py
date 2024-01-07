from django.urls import path
from . import views

urlpatterns = [
    path("",  views.back_office_home, name="back_office_home"),
]

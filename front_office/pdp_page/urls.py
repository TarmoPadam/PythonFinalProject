from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdp_page, name="front_office.pdp_page"),
]
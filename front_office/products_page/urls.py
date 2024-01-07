from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_page, name="front_office.products_page"),
]
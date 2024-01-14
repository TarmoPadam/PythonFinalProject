from django.urls import path
from . import views

urlpatterns = [
    path("",  views.invoices, name="invoices"),
    path('<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
]

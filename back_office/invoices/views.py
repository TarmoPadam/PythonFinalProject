from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.

def invoices(request):
    invoices = models.InvoiceDetail.objects.all()
    return render(request, "invoices.html", {"invoices": invoices})


def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(models.InvoiceDetail, id=invoice_id)
    # You can add more logic here if needed
    return render(request, "invoice_detail.html", {"invoice": invoice})
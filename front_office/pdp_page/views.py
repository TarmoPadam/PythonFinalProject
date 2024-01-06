from django.shortcuts import render, redirect
from back_office.products.models import Product

# Create your views here.

def pdp_page(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "pdp_page.html", 
    {'product': product})
    
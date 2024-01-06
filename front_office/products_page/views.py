from django.shortcuts import render
from back_office.products.models import Product


# Create your views here.

def products_page(request):
    products = Product.objects.all()
    return render(request, "products_page.html",
    {'products': products})
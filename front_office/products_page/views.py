from django.shortcuts import render
from back_office.products.models import Product


# Create your views here.

def products_page(request):
    products = Product.objects.all()
    total_items_in_cart = request.session.get('total_items_in_cart', 0)
    return render(request, "products_page.html",
                  {'products': products,
                   'total_items_in_cart': total_items_in_cart})

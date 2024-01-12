from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Supplier
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required
def products(request):
    if request.user.is_authenticated:
        try:
            supplier = Supplier.objects.get(user=request.user)
            products = Product.objects.filter(
                supplier=supplier).order_by('name')
        except Supplier.DoesNotExist:
            products = Product.objects.none()
    else:
        products = Product.objects.all().order_by('name')

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'backoffice_products.html', {'products': products})


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'backoffice_product_details.html', {'product': product})

from django.db import models
from django.shortcuts import render, redirect
from back_office.orders.models import OrderItem
from django.contrib.auth.decorators import login_required
from back_office.customers.models import UserDetail
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from back_office.products.models import Category, Brand, Product
from back_office.orders.models import Order


@login_required
def cart_view(request):
    user = request.user
    user_detail = UserDetail.objects.get(user=user)
    order, created = Order.objects.get_or_create(order_user=user_detail)
    order_items = order.order_items.all()

    total_items_in_cart = order_items.aggregate(
        total_items=models.Sum('quantity'))['total_items']

    total_order_cost = sum(order_item.item_price for order_item in order_items)

    all_categories = Category.objects.all()
    all_brands = Brand.objects.all()

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            order_item, created = OrderItem.objects.get_or_create(
                order=order, product=product)
            if not created:
                order_item.quantity += 1
            else:
                order_item.quantity = 1
            order_item.save()
            return redirect('shopping_cart_page:show_cart')

    return render(request, 'cart.html', {'order_items': order_items, 'total_items_in_cart': total_items_in_cart, 'all_categories': all_categories, 'all_brands': all_brands, 'total_order_cost': total_order_cost})


@login_required
def update_cart(request):
    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        quantity = int(request.POST.get('quantity'))
        order_item = get_object_or_404(OrderItem, id=order_item_id)
        if 'increment' in request.POST:
            order_item.quantity += 1
            messages.success(
                request, f"{order_item.product.name} quantity increased to {order_item.quantity}")

        elif 'decrement' in request.POST:
            if order_item.quantity > 1:
                order_item.quantity -= 1
                messages.success(
                    request, f"{order_item.product.name} quantity decreased to {order_item.quantity}")
            else:
                messages.success(
                    request, f"Cannot decrease {order_item.product.name} below 1")
        order_item.save()

    return redirect('shopping_cart_page:show_cart')


@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        order_item = get_object_or_404(OrderItem, id=order_item_id)
        order_item.delete()
        messages.success(
            request, f"{order_item.product.name} removed from the cart")
        return redirect('shopping_cart_page:show_cart')
    else:
        return HttpResponseNotAllowed(['POST'])

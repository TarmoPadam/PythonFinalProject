def cart_items_count(request):
    total_items_in_cart = 0
    if 'total_items_in_cart' in request.session:
        total_items_in_cart = request.session['total_items_in_cart']
    return {'total_items_in_cart': total_items_in_cart}

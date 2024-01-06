from django.urls import path
from . import views


app_name = 'shopping_cart_page'

urlpatterns = [
    # URL pattern for the cart_view with the app namespace
    path('', views.cart_view, name='show_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('remove_from_cart/',
         views.remove_from_cart, name='remove_from_cart')
]

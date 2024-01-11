from django.urls import path
from .views import products, product_detail

urlpatterns = [
    path('', products, name='backoffice_products'),
    path('<int:product_id>/', product_detail, name='backoffice_product_detail')
]

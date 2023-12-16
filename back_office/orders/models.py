from django.db import models
from back_office.products.models import Product as order_product
from back_office.products.models import Discount as order_discount


# Create your models here.


class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    list_of_products = models.ManyToManyField(order_product, blank=True)
    complete_cost = models.FloatField(default=0)
    discounts = models.ForeignKey(
        order_discount, on_delete=models.SET_NULL, null=True, blank=True)

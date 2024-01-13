from django.db import models
import random
from back_office.products.models import Product
from back_office.products.models import Discount as order_discount
from back_office.customers.models import UserDetail

# Create your models here.


class InvoiceDetail(models.Model):
    invoice_number = models.PositiveIntegerField(default=random.randint(0,9999))
    customer = models.OneToOneField(UserDetail, on_delete=models.SET_NULL, null=True)
    list_of_products = models.ManyToManyField(Product, blank=True)
    order_discount = models.OneToOneField(order_discount, on_delete=models.SET_NULL, null=True, blank= True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'invoice{self.invoice_number}'
    
    
    
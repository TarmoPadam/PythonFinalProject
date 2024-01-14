from django.db import models
from back_office.products.models import Product as user_product
from django.contrib.auth.models import User

# Create your models here.


class SupplierDetail(models.Model):
    total_amount_spent = models.FloatField(default=0)
    total_orders_completed = models.PositiveIntegerField(default=0)
    user_products = models.ManyToManyField(user_product, blank=True)
    supplier = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.supplier.first_name} {self.supplier.last_name}'

    class Meta:
        verbose_name = "Supplier"

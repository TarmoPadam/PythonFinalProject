from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(
        'Brands', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        'Categories', on_delete=models.SET_NULL, null=True, blank=True)
    amount_sold = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(
        'Discount', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.ForeignKey('Supplier', on_delete=models.SET_NULL,
                              null=True, blank=True)


class Categories(models.Model):
    title = models.CharField(max_length=255)
    list_of_products = models.ManyToManyField(Product)
    list_of_brands = models.ManyToManyField('Brands')


class Brands(models.Model):
    title = models.CharField(max_length=255)
    list_of_products = models.ManyToManyField(Product)
    list_of_categories = models.ManyToManyField(Categories)


class Supplier(models.Model):
    title = models.CharField(max_length=255)
    products_list = models.ManyToManyField(Product)
    list_of_brands = models.ManyToManyField(Brands)
    list_of_categories = models.ManyToManyField(Categories)
    min_price = models.FloatField()
    max_price = models.FloatField()


class Discount(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

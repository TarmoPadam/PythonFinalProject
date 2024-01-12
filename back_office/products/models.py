from django.db import models
from django.db.models import DecimalField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, max_length=350)
    details = models.TextField(null=True, blank=True, max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[
                                MinValueValidator(0.0)])
    image = models.ImageField(
        upload_to='uploads/product/', blank=True, null=True)
    in_stock = models.BooleanField(default=False)
    amount_sold = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(
        'Brand', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.ForeignKey(
        'Discount', on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category', blank=True)
    products = models.ManyToManyField(
        Product, related_name='categories', blank=True)
    brands = models.ManyToManyField('Brand', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=255)
    brands = models.ManyToManyField('Brand', blank=True)
    products = models.ManyToManyField(
        Product, related_name='brands', blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(
        Product, related_name='suppliers', blank=True)
    brands = models.ManyToManyField(Brand, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    min_price = models.FloatField()
    max_price = models.FloatField()

    def __str__(self):
        return self.name


class Discount(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

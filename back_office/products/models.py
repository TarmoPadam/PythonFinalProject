from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
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
    products = models.ManyToManyField(
        Product, related_name='categories', blank=True)
    brands = models.ManyToManyField('Brand', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(
        Product, related_name='brands', blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
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

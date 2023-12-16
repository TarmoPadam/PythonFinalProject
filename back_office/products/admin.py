from django.contrib import admin
from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "supplier")


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Discount)
admin.site.register(models.Supplier)

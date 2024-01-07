from django.contrib import admin
from . import models
from .models import Order, OrderItem

# Register your models here.


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('order_number', 'title',
#                     'date', 'complete_cost', 'order_user')
# # #     # list_display = ('title', 'date', 'complete_cost')


# admin.site.register(models.OrderItem)
# admin.site.register(models.Order, OrderAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of extra OrderItem forms to display


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)


admin.site.register(Order, OrderAdmin)

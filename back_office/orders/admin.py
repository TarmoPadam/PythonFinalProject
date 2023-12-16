from django.contrib import admin
from . import models

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'complete_cost')


admin.site.register(models.Order, OrderAdmin)

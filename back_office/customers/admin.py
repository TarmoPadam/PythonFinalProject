from django.contrib import admin
from . import models

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name',
                    'total_orders_completed', 'total_amount_spent')

    def get_user_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else "N/A"

    get_user_full_name.short_description = 'User'


admin.site.register(models.UserDetail, CustomerAdmin)

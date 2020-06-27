from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        ''
    ]
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
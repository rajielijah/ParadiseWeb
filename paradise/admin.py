from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'recieved',
    ]    
    list_display_links = [
        'user',
        'ordered'
    ]
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Group)
admin.site.register(Prize)
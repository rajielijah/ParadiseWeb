from django.contrib import admin
from .models import *


class CompetitionAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('title', 'slug', 'description')
    list_display_links = ('title', 'description')
    list_editable = ('slug',)
    search_fields = ('title', 'slug')
    filter_horizontal = ('prize_to_win', 'belong_to')
    list_filter = ('isActive', 'isFeatured')


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Prize)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Competition_Group)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)

from django.contrib import admin
from .models import *

class SellAdmin(admin.ModelAdmin):
    list_display = ['customer','created_at','discount_cc','discount_ci','delivery', 'money_received','note','updated_at']
    list_per_page = 10
admin.site.register(Sell,SellAdmin)

class SellItemAdmin(admin.ModelAdmin):
    list_display = ['sell','product','quantity']
    list_editable = ['product','quantity']
    list_per_page = 10
admin.site.register(SellItem,SellItemAdmin)

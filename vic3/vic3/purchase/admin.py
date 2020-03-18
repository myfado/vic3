from django.contrib import admin

from .models import Vendor, Purchase, PurchaseItem

class VendorAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Vendor,VendorAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['created_at','vendor','discount','payment','note','updated_at']
    list_editable = ['vendor','discount','payment','note']
    list_per_page = 10
admin.site.register(Purchase,PurchaseAdmin)

class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['purchase','product','quantity']
    list_editable = ['product','quantity']
    list_per_page = 10
admin.site.register(PurchaseItem,PurchaseItemAdmin)

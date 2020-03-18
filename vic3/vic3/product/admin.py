from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','points','stock','updated_at']
    list_editable = ['price','stock']
    list_per_page = 10
admin.site.register(Product,ProductAdmin)

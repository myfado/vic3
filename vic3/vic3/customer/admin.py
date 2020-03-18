from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['f_name','l_name', 'city', 'status']

admin.site.register(Customer, CustomerAdmin)

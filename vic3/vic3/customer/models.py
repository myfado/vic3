from django.db import models
from django.urls import reverse

class Customer(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=30)
    city = models.CharField(max_length=20,blank=True)
    STATUS = (
        ('CU', 'Customer'),
        ('MA', 'Manager'),
        ('DI', 'Distributor'),
        )
    status = models.CharField(max_length=2,choices=STATUS,default='CU')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'customer'
        ordering = ('city','l_name','f_name','status')

    def __str__(self):
        return self.f_name + ' '+ self.l_name + ' '+ self.city+ ' '+ self.status

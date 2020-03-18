from django.db import models
from django.urls import reverse


class Product(models.Model):
    PRODUCER = (
        ('CC', 'Colway Classic'),
        ('CI', 'Colway International'),
        ('NC', 'Non Colway'),
    )
    producer = models.CharField(max_length=2,choices=PRODUCER)
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    points = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    discontinued = models.BooleanField(default=False)
    link = models.URLField(blank=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'product'
        ordering = ('producer','name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        if  self.discontinued==True:
            return self.get_producer_display() + '  '+ self.name + '   '+ str(self.price) + '  (discontinued!) '
        else:
            return self.name + '   ' + str(self.producer)+'  ' +str(self.price)

    def get_absolute_url(self):
        return reverse('product:product-detail', {'id':self.id})

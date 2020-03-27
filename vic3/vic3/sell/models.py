from django.db import models
from product.models import Product
from customer.models import Customer


class Sell(models.Model):
    customer = models.ForeignKey(Customer, null=True, related_name="has_sales",on_delete=models.SET_NULL)
    DISCOUNT_CC = [(x, x) for x in range (0, 43)]
    discount_cc = models.PositiveSmallIntegerField(choices=DISCOUNT_CC, default=0)
    DISCOUNT_CI = [(y, y) for y in range (0, 41)] 
    discount_ci = models.PositiveSmallIntegerField(choices=DISCOUNT_CI, default=0)
    DELIVERY = (
        ('HD', 'To Hand'),
        ('CD', 'Cash on Delivery Post'),
        ('PO', 'No Cash Post'),
    )
    delivery = models.CharField(max_length=2,choices=DELIVERY, default='HD')
    money_received = models.BooleanField(default=False)
    note = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sell'
        ordering = ('-created_at','-updated_at')
        verbose_name_plural = "Sales"
    def __str__(self):
        return str(self.customer) + '  ' +str(self.created_at) + '  ' +self.get_delivery_display()+ ' updated_on: ' + str(self.updated_at)

class SellItem(models.Model):
    sell = models.ForeignKey(Sell, related_name="has_items",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, related_name="product_sells",on_delete=models.SET_NULL)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'sellitem'
        ordering = ('-sell',)
        verbose_name_plural = "SellItems"

    def __str__(self):
        return str(self.sell)

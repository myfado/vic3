from django.db import models
from product.models import Product

class Vendor(models.Model):
    name = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'vendor'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='purchases', blank=True, null=True, on_delete=models.SET_NULL)
    DISCOUNT = (
        (50, '50%'),
        (42, '42%'),
        (40, '40%'),
        (30, '30%'),
        (20, '20%'),
        (10, '10%'),
        (0, '0%'),
    )
    discount = models.PositiveSmallIntegerField(choices=DISCOUNT, default=42)
    PAYMENT = (
        ('CD', 'Card'),
        ('CS', 'Cash'),
        ('CR', 'Credit'),
    )
    payment = models.CharField(max_length=2,choices=PAYMENT, default='CS')
    note = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'purchase'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.created_at) + '  ' + str(self.vendor) + '  '+ self.get_discount_display() + '  ' + self.get_payment_display() + ' updated_on: ' + str(self.updated_at)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name="has_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, verbose_name="Item", on_delete=models.SET_NULL)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'purchaseitem'
        ordering = ('-purchase',)

    def __str__(self):
        return str(self.purchase)

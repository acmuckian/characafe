from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
import uuid
from django.core.validators import MinValueValidator
from products.models import Product

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    email = models.EmailField(blank=False, null=False)
    name = models.CharField(max_length=200, unique=False, blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    street_address = models.CharField(max_length=500, null=False, blank=False, default="")
    town_or_city = models.CharField(max_length=100, null=False, blank=False, default="")
    county = models.CharField(max_length=100, null=False, blank=False, default="")
    postcode = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')



    def generate_order_number(self):
        """
        generate random order number of 32 characters
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """Update grand total each time a line item is added, accounting for delivery costs."""
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    
    def save(self, *args, **kwargs):
        """Override the original save method to set the order number if it hasn't been set already."""
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1,  validators=[MinValueValidator(1)])
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """Override the original save method to set the lineitem total and update the order total."""
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.product.name} (x{self.quantity}) on order {self.order.order_number}'




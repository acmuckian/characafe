from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator
from products.models import Product

# Create your models here.

class Order(models.Model):
    email = models.EmailField(blank=False, null=False)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_city = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0,  validators=[MinValueValidator(1)])
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)




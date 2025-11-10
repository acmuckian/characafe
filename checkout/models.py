from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
import uuid
from django.core.validators import MinValueValidator
from products.models import Product
from profiles.models import Profile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="orders",
    )
    email = models.EmailField()
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
    )
    order_total = models.DecimalField(  # keep only one definition
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )
    country = CountryField(blank_label="Country *")
    street_address = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        default="",
    )
    town_or_city = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="",
    )
    county = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="",
    )
    postcode = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )
    original_bag = models.TextField(default="")
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default="",
    )

    def generate_order_number(self):
        """Generate a random 32 char order number."""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update grand total each time a line item is added."""
        agg = self.lineitems.aggregate(total=Sum('lineitem_total'))
        self.order_total = agg['total'] or 0
        threshold = settings.FREE_DELIVERY_THRESHOLD
        percentage = settings.STANDARD_DELIVERY_PERCENTAGE
        if self.order_total < threshold:
            self.delivery_cost = (self.order_total * percentage) / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
    )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) on order"

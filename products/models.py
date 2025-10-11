from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(max_length=1000, unique=True, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    character = category = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='products'
    )
    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User
from home.models import Character
# Create your models here.



class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(max_length=1000, unique=True, blank=False, null=False)
    details = models.TextField(max_length=1000, unique=True, blank=False, null=False, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='products'
    )
    def __str__(self):
        return self.name


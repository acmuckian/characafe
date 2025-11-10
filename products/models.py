from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from home.models import Character

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(
        max_length=1000, unique=True, blank=False, null=False)
    details = models.TextField(
        max_length=1000, unique=False, blank=False, null=False, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    wishlist = models.ManyToManyField(
        User, related_name='wishlist',  blank=True)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments")
    created_on = created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField(
        max_length=1000, blank=False, null=False, default="")

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.commenter}"

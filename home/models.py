from django.db import models
from django.db.models.functions import Now


# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='characters/', blank=True, null=True)
    description = models.CharField(max_length=1000, unique=True, blank=False, null=False)
    birthday = models.DateField(db_default=Now())
    colour = models.CharField(max_length=200, blank=False, null=False, default="Red")
    likes = models.CharField(max_length=200, unique=True, blank=False, null=False, default=None)
    dislikes = models.CharField(max_length=200, unique=True, blank=False, null=False, default=None)

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    description = models.CharField(max_length=1000, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
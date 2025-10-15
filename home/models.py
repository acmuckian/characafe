from django.db import models


# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    image = models.ImageField()
    description = models.CharField(max_length=1000, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(blank=False, null=False, default="Name", max_length=200)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(blank=False, null=False, default="Subject line", max_length=200)
    body = models.TextField(blank=False, null=False, default="", max_length=1500)

    def __str__(self):
        return f"Contact request from {self.name}"
    
class Newsletter(models.Model):
     email = models.EmailField(blank=False, null=False)
     date_created = models.DateField(auto_now_add=True)


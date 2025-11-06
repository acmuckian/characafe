from django.contrib import admin
from .models import Profile 
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
    'default_phone_number',
    'default_street_address',
    'default_town_or_city',
    'default_county',
    'default_postcode',
    'default_country',
    )

admin.site.register(Profile, ProfileAdmin)

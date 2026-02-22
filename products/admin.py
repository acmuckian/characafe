from django.contrib import admin
from .models import Product, Comment
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'character',
        'price',
        'rating',
        'image',
    )

    ordering = ('slug',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)

from django.contrib import admin
from products.models import Products, Category, Carts

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Carts)

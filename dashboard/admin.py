from django.contrib import admin
from .models import Product
from .models import Order
from django.contrib.auth.models import Group

admin.site.site_header = "Victoria's StockControl --> Admin"

class ProductTabulatedAdmin(admin.ModelAdmin):
    list_display =('name','category','quantity')
    list_filter = ['category']

class OrderTabulatedAdmin(admin.ModelAdmin):
    list_display =('product','staff','order_quantity','date')
    list_filter = ['staff']

# Register your models here.

admin.site.register(Product, ProductTabulatedAdmin)
admin.site.register(Order, OrderTabulatedAdmin)
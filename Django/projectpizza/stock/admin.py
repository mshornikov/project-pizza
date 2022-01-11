from re import search
from django.contrib import admin
from django.contrib import admin
from django.db import models

from .models import Stock
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock_key', 'stock_product', 'stock_value')
    search_fields = ('id', 'stock_key', 'stock_product', 'stock_value')

admin.site.register(Stock, StockAdmin)

from re import search
from django.contrib import admin
from django.contrib import admin
from django.db import models

from .models import Stock
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_key', 'stock_product', 'stock_value', 'stock_type' )
    search_fields = ('stock_key', 'stock_product', 'stock_value',  'stock_type')

admin.site.register(Stock, StockAdmin)

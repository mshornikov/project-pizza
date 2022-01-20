from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'discription', 'image', 'cost', 'category')
    search_fields = ('id', 'name', 'cost', 'category')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

from django.contrib import admin
from .models import *
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name', 'email', 'address', 'city', 'created', 'paid']
    list_filter = ['paid', 'city', 'email']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

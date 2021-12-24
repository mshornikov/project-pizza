from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return ProductCategory.objects.all()

@register.simple_tag()
def get_product_on_category(find_cat):
    return Product.objects.filter(category=find_cat)
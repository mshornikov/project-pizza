from rest_framework import serializers
from .models import *

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'category')

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'discription', 'cost', 'category')

class ProductOnCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'discription', 'cost')

class ProductOnCartDetailSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField('get_product_quantity')

    def get_product_quantity(self, product_object):
        pass

    class Meta:
        model = Product
        fields = ('name', 'discription', 'cost', 'quantity')

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('name',)

class CategoryDetailSerializer(serializers.ModelSerializer):
    product_list = serializers.SerializerMethodField('get_product_list')
    def get_product_list(self, category_object):
        return [ProductOnCategoryDetailSerializer(product).data for product in Product.objects.filter(category=category_object.id)]

    class Meta:
        model = ProductCategory
        fields = ('name', 'product_list')
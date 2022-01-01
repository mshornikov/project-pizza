from rest_framework import serializers
from .models import *

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'discription', 'image', 'cost', 'category')

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'discription', 'image', 'cost', 'category')

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('name',)


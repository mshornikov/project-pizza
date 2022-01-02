from rest_framework import serializers
from .models import *



class ProductOnCartDetailSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField('get_product_quantity')

    def get_product_quantity(self, product_object):
        pass

    class Meta:
        model = Product
        fields = ('name', 'discription', 'cost', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'discription', 'image', 'cost', 'category')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('name',)
from rest_framework import serializers


from .models import *
from main.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


# class OrderItemSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OrderItems
#         fields = fields = "__all__"

    
class OrderItemSerializer(serializers.ModelSerializer):
    total_point_price = serializers.SerializerMethodField('get_total_point_price')
    product_info = serializers.SerializerMethodField('get_product_info')

    def get_total_point_price(self, order_item_object):
        return order_item_object.price * order_item_object.quantity
    
    def get_product_info(self, order_item_object):
        return ProductSerializer(order_item_object.product).data
        
    class Meta:
        model = OrderItems
        fields = ('order', 'product_info', 'quantity', 'total_point_price')
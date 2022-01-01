from rest_framework import serializers
from .models import *

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'total_cost',)

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ('id','order',)

    
class OrderItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        # fields = ('id', 'order', 'product')
        fields = "__all__"
from rest_framework import serializers
from main.models import Product
from main.serializers import ProductSerializer

class CartDetailSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length = 200)
    product_list = serializers.SerializerMethodField('get_product_list')

    def get_product_list(self, cart_object):
        cart_id_list = [int(id) for id in cart_object.cart.keys()]
        product_list = Product.objects.filter(id__in=cart_id_list)
        result_data = []
        for product in product_list:
            temp = ProductSerializer(product).data
            temp['quantity'] = cart_object.cart[str(product.id)]['quantity']
            result_data.append(temp)
        return result_data 
    
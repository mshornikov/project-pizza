from rest_framework import serializers
from main.models import *
from orders.models import *
from stock.models import *
from vacancy.models import *
from django.contrib.auth import get_user_model

from users.models import CustomUser

# <----SESSION CART---->


# <----PRODUCT AND CATEGORY---->
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

class StockProductOnCartDetailSerializer(serializers.ModelSerializer):

    def get_product_quantity(self, product_object):
        pass

    class Meta:
        model = Product
        fields = ('name', 'discription', 'cost')

class CartSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length = 200)
    product_list = serializers.SerializerMethodField('get_product_list')

# def get_product_list(self, cart_object):
# cart_id_list = [int(id) for id in cart_object.cart.keys()]
# product_list = Product.objects.filter(id__in=cart_id_list)
# result_data = []
# for product in product_list:
# temp = ProductSerializer(product).data
# temp['quantity'] = cart_object.cart[str(product.id)]['quantity']
# result_data.append(temp)
# return result_data
    def get_product_list(self, cart_object):
        result_data = {'default':[], 'stock_cart':[]}
        default_cart_ids = [int(id) for id in cart_object.cart['default'].keys()]
        stock_cart_ids = [int(id) for id in cart_object.cart['stock_cart'].keys()]

        default_product_list = Product.objects.filter(id__in=default_cart_ids)
        stock_cart_product_list = Product.objects.filter(id__in=stock_cart_ids)

        for product in default_product_list:
            temp = ProductSerializer(product).data
            temp['quantity'] = cart_object.cart['default'][str(product.id)]['quantity']
            result_data['default'].append(temp)

        for product in stock_cart_product_list:
            temp = StockProductOnCartDetailSerializer(product).data
            temp['quantity'] = 1
            result_data['stock_cart'].append(temp)

        return result_data


# <----ORDER AND ORDERITEMS---->
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

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

# <----CUSTOM USER---->
UserModel = get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user( username=validated_data['username'], password=validated_data['password'],)
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'password')

# <----STOCK---->
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

# <----Vacancy---->
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
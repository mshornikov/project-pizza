from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, request
from django.utils.translation import templatize
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.
from .models import *
from .utils import DataMixin
from cart.forms import CartAddProductForm
from orders.models import Order

class MainPageView(DataMixin, TemplateView):
    template_name = "main/mainPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.ProjectPizza'))
        cat_list = {product_category:Product.objects.filter(category=product_category) for product_category in ProductCategory.objects.all()}
        context['cat_list'] = cat_list
        context['cart_product_form'] = CartAddProductForm()
        return context

class StockPageView(DataMixin, TemplateView):
    template_name = 'main/stockPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.Stocks'))
        return context

class AboutPageView(DataMixin, TemplateView):
    template_name = 'main/aboutPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.About'))
        return context

class ContactsPageView(DataMixin, TemplateView):
    template_name = 'main/contactsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.Contacts'))
        return context 

class ProfilePageView(DataMixin, TemplateView):
    template_name = 'main/profilePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.Profile'))
        context['orders'] = Order.objects.filter(user_id=self.request.user.id)
        return context 

class PageNotFoundView(DataMixin, TemplateView):
    template_name = 'main/404page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.NotFound'))
        return context 


#  <------------------------------------------>
#  <-----------Rest Framework Views----------->

class ProductListView(APIView):
    """Вывод списка товаров"""
    def get(self, request):
        product_list = Product.objects.all()
        serializer = ProductListSerializer(product_list, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    """Характеристика одного товара"""
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

class CategoryListView(APIView):
    """Вывод списка категорий товаров"""
    def get(self, request):
        category_list = ProductCategory.objects.all()
        serializer = CategoryListSerializer(category_list, many=True)
        return Response(serializer.data)

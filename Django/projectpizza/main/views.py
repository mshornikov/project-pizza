from math import prod
from unicodedata import category, name
from django.views.generic.base import TemplateView
# Create your views here.
from .models import *
from projectpizza.utils import DataMixin
from cart.forms import CartAddProductForm

class MainPageView(DataMixin, TemplateView):
    template_name = "main/mainPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))

        cat_list = {}
        for product_category in ProductCategory.objects.all():
            if product_category.name != 'Комбо':
                cat_list[product_category] = Product.objects.filter(category=product_category)

        context['cat_list'] = cat_list
        context['cart_product_form'] = CartAddProductForm()
        context['selected_page'] = 'Меню'
        return context

class StockPageView(DataMixin, TemplateView):
    template_name = 'main/stockPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        context['selected_page'] = 'Комбо'
        try:
            
            cata = ProductCategory.objects.get(name='Комбо')
            context['product_list'] = Product.objects.filter(category=cata)
        except:
            pass
        context['cart_product_form'] = CartAddProductForm()
        return context

class AboutPageView(DataMixin, TemplateView):
    template_name = 'main/aboutPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        context['selected_page'] = 'О нас'
        return context

class ContactsPageView(DataMixin, TemplateView):
    template_name = 'main/contactsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        context['selected_page'] = 'Контакты'
        return context 

class PageNotFoundView(DataMixin, TemplateView):
    template_name = 'main/404page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.NotFound'))
        return context 



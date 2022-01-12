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
        cat_list = {product_category:Product.objects.filter(category=product_category) for product_category in ProductCategory.objects.all()}
        context['cat_list'] = cat_list
        context['cart_product_form'] = CartAddProductForm()
        return context

class StockPageView(DataMixin, TemplateView):
    template_name = 'main/stockPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        return context

class AboutPageView(DataMixin, TemplateView):
    template_name = 'main/aboutPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        return context

class ContactsPageView(DataMixin, TemplateView):
    template_name = 'main/contactsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        return context 

class VacanciesPageView(DataMixin, TemplateView):
    template_name = 'main/vacanciesPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='ProjectPizza'))
        return context 

class PageNotFoundView(DataMixin, TemplateView):
    template_name = 'main/404page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.NotFound'))
        return context 



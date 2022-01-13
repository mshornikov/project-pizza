from django.shortcuts import render
from projectpizza.utils import DataMixin
from django.views.generic.base import TemplateView
from .models import Vacancy
# Create your views here.

class VacanciesPageView(DataMixin, TemplateView):
    template_name = 'vacancy/vacanciesPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.ProjectPizza'))
        que_set = Vacancy.objects.filter(is_open=True)
        context['vacancies'] = Vacancy.objects.filter(is_open=True)
        context['length'] = len(que_set)
        return context 
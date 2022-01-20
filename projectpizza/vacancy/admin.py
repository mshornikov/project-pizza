from re import search
from django.contrib import admin
from .models import Vacancy
# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'discription', 'salary', 'is_open')
    search_fields = ('profession', 'salary', 'is_open')

admin.site.register(Vacancy, VacancyAdmin)


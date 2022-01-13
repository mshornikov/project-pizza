from django.db import models

# Create your models here.

class Vacancy(models.Model):
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    discription = models.CharField(max_length=400, verbose_name='Предложение')
    salary = models.IntegerField(default=10000, verbose_name='Заработная плата')
    image = models.ImageField(upload_to='VacancyImages', verbose_name='Фото')
    is_open = models.BooleanField(default=True, verbose_name='Актуальность')
    
    def __str__(self):
        return self.profession

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']
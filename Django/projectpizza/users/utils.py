# Класс данных, передающий общий контекст страницы
menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
]



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
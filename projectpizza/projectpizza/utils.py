menu = [
    {'title': "Меню", 'url': 'home'},
    {'title': "Комбо", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
    

]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
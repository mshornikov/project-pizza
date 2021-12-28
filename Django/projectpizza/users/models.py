from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils import timezone

# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, phone, password, **fields):
        values = [email, first_name, last_name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for feild_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(feild_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, first_name, last_name, phone, password=None, **fields):
        fields.setdefault('is_staff', False)
        fields.setdefault('is_supreuser', False)
        return self._create_user(self, email, first_name, last_name, phone, password=None, **fields)
    
    def create_superuser(self, email, first_name, last_name, phone, password, **fields):
        fields.setdefault('is_staff', True)
        fields.setdefault('is_supreuser', True)

        if fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(self, email, first_name, last_name, phone, password, **fields)


# Опрделение собственной модели пользователя с дополнительными полями:
# Почта, день рождения, телефон. Уникальность пользователя определена полем Почта
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождения')
    is_staff = models.BooleanField(default=False, verbose_name='Право доступа')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')
    last_login = models.DateTimeField(null=True, verbose_name='Последний вход')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
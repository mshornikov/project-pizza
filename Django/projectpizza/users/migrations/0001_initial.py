# Generated by Django 3.2.9 on 2021-12-28 17:03

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Право доступа')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('last_login', models.DateTimeField(null=True, verbose_name='Последний вход')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]

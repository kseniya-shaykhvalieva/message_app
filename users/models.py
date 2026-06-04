from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', help_text='Введите Вашу Фамилию')
    first_name = models.CharField(max_length=150, verbose_name='Имя', help_text='Введите Ваше имя')
    patronymic = models.CharField(max_length=150, blank=True, null=True, verbose_name='Отчество',
                                  help_text='Введите Ваше отчество (необязательное поле)')

    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите Ваш email')

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите фотографию')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон',
                                    help_text='Введите Ваш номер телефона')
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}, email: {self.email}'

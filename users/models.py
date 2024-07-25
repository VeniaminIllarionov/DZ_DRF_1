from django.contrib.auth.models import AbstractUser
from django.db import models

from material.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='users/photo', verbose_name='Аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True,
                             null=True, help_text='Введите номер телефона')
    city = models.CharField(max_length=35, verbose_name='Страна', blank=True,
                            null=True, help_text='Введите страну')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'


class Payments(models.Model):
    method_variants = (
        ('cash', 'наличные'),
        ('transfer', 'перевод'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.PositiveSmallIntegerField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    payment_amount = models.PositiveBigIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=80, choices=method_variants, default='transfer',
                                      verbose_name='способ оплаты')
    session_id = models.CharField(max_length=255, verbose_name='Id сессии', blank=True,
                                   null=True)
    link_payment = models.URLField(max_length=400, verbose_name='Ссылка на оплату', blank=True,
                                   null=True, help_text='Введите ссылку на оплату')

    def __str__(self):
        return f'Оплата для {self.user}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ('-date_payment',)

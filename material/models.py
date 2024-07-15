from django.db import models

from config import settings



class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='material/course', verbose_name='Картинка', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создал')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс',blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='material/lesson', blank=True, null=True, verbose_name='Картинка')
    url_video = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создал')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('title',)


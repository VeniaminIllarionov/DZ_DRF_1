# Generated by Django 4.2 on 2024-07-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='link_payment',
            field=models.URLField(blank=True, help_text='Введите ссылку на оплату', max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
    ]

# Generated by Django 4.2 on 2024-07-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='message',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Сообщение'),
        ),
    ]

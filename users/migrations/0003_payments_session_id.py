# Generated by Django 4.2 on 2024-07-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payments_link_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Id сессии'),
        ),
    ]

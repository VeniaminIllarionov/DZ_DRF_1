# Generated by Django 4.2 on 2024-07-23 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_subscription_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='message',
        ),
    ]

import datetime

from celery import shared_task

from users.models import User


@shared_task
def check_user_activity():
    """
    Проверяем активность пользователя, если больше 30 дней, деактивируем
    """
    users = User.objects.all()
    date_now = datetime.date.today()
    for user in users:
        if date_now > user.last_login:
            user.is_active = False
            user.save()
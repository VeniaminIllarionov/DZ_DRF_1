from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='test3@example.com')
        user.is_staff = True
        user.is_active = True
        user.is_superuser = False
        user.set_password('0205')
        user.save()

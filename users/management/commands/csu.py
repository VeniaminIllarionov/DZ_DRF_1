from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='venya957@gmail.com')
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.set_password('0205')
        user.save()

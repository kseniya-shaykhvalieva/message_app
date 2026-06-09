import os
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from dotenv import load_dotenv


load_dotenv()

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(email=os.getenv('SUPER_USER_EMAIL'))

        user.set_password(os.getenv('SUPER_USER_PASSWORD'))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Суперпользователь успешно создан'))

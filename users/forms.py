from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'password1', 'password2',)

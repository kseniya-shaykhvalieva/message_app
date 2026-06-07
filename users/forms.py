from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'password1', 'password2',)


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control text-center',
            'placeholder': 'Введите вашу электронную почту в это поле'
        })

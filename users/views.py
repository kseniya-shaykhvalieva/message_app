import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView

from config.settings import DEFAULT_FROM_EMAIL
from users.forms import UserRegisterForm
from users.models import CustomUser


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomUser
    permission_required = 'users.can_block_user'
    template_name = 'users/user_list.html'


class UserBlockView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = CustomUser
    permission_required = 'users.can_block_user'

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.is_active = not user.is_active
        user.save()
        return redirect('users:user_list')


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Здравствуйте! Спасибо, что зарегистрировались на нашем сайте. Для подтверждения почты перейдите по ссылке: {url}',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
        user = get_object_or_404(CustomUser,token=token)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))

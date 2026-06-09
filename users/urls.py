from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.forms import CustomPasswordResetForm
from users.views import UserCreateView, email_verification, UserListView, UserBlockView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_block/<int:pk>/', UserBlockView.as_view(), name='user_block'),
    path('password_reset_form/',
         PasswordResetView.as_view(form_class=CustomPasswordResetForm, template_name='reg/password_reset_form.html',
                                   email_template_name='reg/password_reset_email.html',
                                   success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='reg/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reg/password_reset_confirm.html',
                                                                     success_url=reverse_lazy(
                                                                         'users:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='reg/password_reset_complete.html'),
         name='password_reset_complete'),
]

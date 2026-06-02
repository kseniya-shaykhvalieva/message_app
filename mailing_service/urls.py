from django.urls import path

from mailing_service.apps import MailingServiceConfig
from mailing_service.views import RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView, \
    RecipientDeleteView

app_name = MailingServiceConfig.name

urlpatterns = [
    path('recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient_list/detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipient_list/create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient_list/detail/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient_list/detail/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
]

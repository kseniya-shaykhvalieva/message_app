from django.urls import path

from mailing_service.apps import MailingServiceConfig
from mailing_service.views import RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView, \
    RecipientDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailingServiceConfig.name

urlpatterns = [
    path('recipients/', RecipientListView.as_view(), name='recipient_list'),
    path('recipients/detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipients/create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipients/detail/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipients/detail/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/detail/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/detail/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]

from django.urls import path

from mailing_service.apps import MailingServiceConfig
from mailing_service.views import RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView, \
    RecipientDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, HomeTemplateView, \
    SendMailingView, StatisticsTemplateView

app_name = MailingServiceConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
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
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/detail/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/detail/<int:pk>/send/', SendMailingView.as_view(), name='send'),
    path('statistics/', StatisticsTemplateView.as_view(), name='statistics'),
]

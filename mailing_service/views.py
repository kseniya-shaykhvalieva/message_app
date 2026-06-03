from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from mailing_service.forms import RecipientForm, MessageForm, MailingForm
from mailing_service.models import Recipient, Message, Mailing
from mailing_service.services import send_mailing


class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailing_service:recipient_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing_service:message_list')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()
        return obj


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_service:mailing_list')


class SendMailingView(View):
    def post(self, request, pk):
        send_mailing(pk)
        return redirect('mailing_service:mailing_list')

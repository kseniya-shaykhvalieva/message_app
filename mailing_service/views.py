from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing_service.forms import RecipientForm, MessageForm, MailingForm
from mailing_service.models import Recipient, Message, Mailing, MailingAttempt
from mailing_service.services import send_mailing


class HomeTemplateView(TemplateView):
    template_name = 'mailing_service/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_count'] = Mailing.objects.count()
        context['active_count'] = Mailing.objects.filter(status=Mailing.STARTED).count()
        context['unique_recipients_count'] = Recipient.objects.count()
        return context


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailing_service:recipient_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing_service:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()
        obj.save()
        return obj


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:mailing_list')
    
    def form_valid(self, form):
        mailing = form.save(commit=False)
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_service:mailing_list')


class SendMailingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        send_mailing(pk)
        return redirect('mailing_service:mailing_list')


class StatisticsTemplateView(TemplateView):
    template_name = 'mailing_service/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner_mailing = Mailing.objects.filter(owner=self.request.user)
        context['success_count'] = MailingAttempt.objects.filter(mailing__in=owner_mailing, status=MailingAttempt.SUCCESS).count()
        context['failed_count'] = MailingAttempt.objects.filter(mailing__in=owner_mailing, status=MailingAttempt.FAILED).count()
        context['message_count'] = Message.objects.filter(mailing__in=owner_mailing).count()
        return context

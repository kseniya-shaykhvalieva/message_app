from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing_service.forms import RecipientForm, MessageForm, MailingForm
from mailing_service.mixin import UserIsOwnerOrManagerMixin
from mailing_service.models import Recipient, Message, Mailing, MailingAttempt
from mailing_service.services import send_mailing


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'mailing_service/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_count'] = Mailing.objects.count()
        context['active_count'] = Mailing.objects.filter(status=Mailing.STARTED).count()
        context['unique_recipients_count'] = Recipient.objects.count()
        return context


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('mailing_service.can_deactivate_mailing'):
            return Recipient.objects.all()
        else:
            return Recipient.objects.filter(owner=user)


class RecipientDetailView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DetailView):
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')

    def form_valid(self, form):
        recipient = form.save(commit=False)
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailing_service:recipient_list')


class RecipientDeleteView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailing_service:recipient_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('mailing_service.can_deactivate_mailing'):
            return Message.objects.all()
        else:
            return Message.objects.filter(owner=user)


class MessageDetailView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')

    def form_valid(self, form):
        message = form.save(commit=False)
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_service:message_list')


class MessageDeleteView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing_service:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('mailing_service.can_deactivate_mailing'):
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(owner=user)


class MailingDetailView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DetailView):
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


class MailingUpdateView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_service:mailing_list')


class MailingDeleteView(LoginRequiredMixin, UserIsOwnerOrManagerMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_service:mailing_list')


class SendMailingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        send_mailing(pk)
        return redirect('mailing_service:mailing_list')


class MailingToggleActiveView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'mailing_service.can_deactivate_mailing'

    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        mailing.is_active = not mailing.is_active
        mailing.save()
        return redirect('mailing_service:mailing_list')


class StatisticsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'mailing_service/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner_mailing = Mailing.objects.filter(owner=self.request.user)
        context['success_count'] = MailingAttempt.objects.filter(mailing__in=owner_mailing, status=MailingAttempt.SUCCESS).count()
        context['failed_count'] = MailingAttempt.objects.filter(mailing__in=owner_mailing, status=MailingAttempt.FAILED).count()
        context['message_count'] = Message.objects.filter(mailing__in=owner_mailing).count()
        return context

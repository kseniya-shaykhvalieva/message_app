from django import forms
from django.utils import timezone

from mailing_service.models import Recipient, Message, Mailing


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите Фамилию Имя Отчество'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Здесь можете оставить комментарий'
        })


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название темы письма'
        })
        self.fields['body'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш текст для рассылки'
        })


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('message', 'recipients', 'start_time', 'end_time',)

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['recipients'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['start_time'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['end_time'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        now = timezone.now()

        if start_time and end_time:
            if start_time < now:
                self.add_error('start_time', 'Дата старта не должна быть в прошлом')

            elif start_time >= end_time:
                self.add_error('end_time', 'Дата старта должна быть раньше даты окончания')

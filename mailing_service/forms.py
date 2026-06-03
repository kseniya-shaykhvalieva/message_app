from django import forms

from mailing_service.models import Recipient, Message, Mailing


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'

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
        fields = '__all__'

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

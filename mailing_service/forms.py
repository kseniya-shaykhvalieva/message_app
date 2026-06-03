from django import forms

from mailing_service.models import Recipient, Message


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

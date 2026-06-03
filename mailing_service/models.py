from datetime import timezone

from django.db import models


class Recipient(models.Model):
    """Получатель"""
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['name']


class Message(models.Model):
    """Сообщение"""
    subject = models.CharField(max_length=250, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject']


class Mailing(models.Model):
    """Рассылка"""
    CREATED = 'created'
    STARTED = 'started'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name='Дата и время первой отправки')
    end_time = models.DateTimeField(verbose_name='Дата и время окончания отправки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение',
                                help_text='Выберете нужное письмо')
    recipients = models.ManyToManyField(Recipient, related_name='mailings')

    def update_status(self):
        """Проверка статуса на текущую дату """
        now = timezone.now()
        if now < self.start_time:
            self.status = self.CREATED
        elif now >= self.end_time:
            self.status = self.COMPLETED
        else:
            self.status = self.STARTED

    def __str__(self):
        return f'Рассылка "{self.message.subject}" - статус: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['message']


class MailingAttempt(models.Model):
    """Попытка рассылки"""
    SUCCESS = 'success'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (SUCCESS, 'Успешно'),
        (FAILED, 'Не успешно'),
    ]
    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    server_response = models.TextField(verbose_name='Ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Рассылка')

    def __str__(self):
        return f'Попытка рассылки "{self.mailing.message.subject}" - статус: {self.status}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['status']

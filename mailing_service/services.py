from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from .models import Mailing, MailingAttempt
from django.utils import timezone


def send_mailing(mailing_pk):
    mailing = get_object_or_404(Mailing, pk=mailing_pk)
    now = timezone.now()

    if now < mailing.start_time or now > mailing.end_time:
        return False

    recipients = mailing.recipients.all()
    for recipient in recipients:
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email='ksyunyabakkanskaya@yandex.ru',
                recipient_list=[recipient.email],
            )
            status = MailingAttempt.SUCCESS
            response = 'OK'
        except Exception as e:
            status = MailingAttempt.FAILED
            response = str(e)

        MailingAttempt.objects.create(
            mailing=mailing,
            status=status,
            server_response=response,
        )

    return True

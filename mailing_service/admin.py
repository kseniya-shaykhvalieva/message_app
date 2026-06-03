from django.contrib import admin
from .models import Recipient, Message


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment',)
    list_filter = ('name',)
    search_fields = ('name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body',)
    list_filter = ('id',)
    search_fields = ('subject',)

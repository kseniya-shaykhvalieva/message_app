from django.contrib import admin
from .models import Recipient


@admin.register(Recipient)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment',)
    list_filter = ('name',)
    search_fields = ('name', 'email',)

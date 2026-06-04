from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'email','phone_number')
    list_filter = ('id',)
    search_fields = ('email',)

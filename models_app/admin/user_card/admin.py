from django.contrib import admin

from models_app.models import UserCard


@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):
    ...

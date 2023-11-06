from django.contrib import admin

from models_app.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    ...

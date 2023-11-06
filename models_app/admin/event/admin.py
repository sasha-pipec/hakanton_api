from django.contrib import admin

from models_app.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ...

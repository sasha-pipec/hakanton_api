from django.contrib import admin

from models_app.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    ...

from django.contrib import admin

from models_app.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_correct', 'question')

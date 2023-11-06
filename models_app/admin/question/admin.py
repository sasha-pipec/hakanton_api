from django.contrib import admin

from models_app.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ...

from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вопроса")

    class Meta:
        db_table = 'questions'
        app_label = 'models_app'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

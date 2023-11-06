from django.db import models


class Answer(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Вопрос"
    )

    class Meta:
        db_table = 'answers'
        app_label = 'models_app'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

from django.db import models


class Message(models.Model):
    message = models.CharField(
        max_length=255,
        verbose_name="Сообщение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="messages_user",
        verbose_name='Автор сообщения'
    )
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        related_name="messages_chat",
        verbose_name='Комната'
    )

    class Meta:
        db_table = 'messages'
        app_label = 'models_app'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

from django.db import models


class UserCard(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name='user_cards',
        verbose_name="Игрок"
    )
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        related_name='rooms',
        verbose_name="Комната"
    )
    card = models.ForeignKey(
        "Card",
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name="Карточка"
    )

    class Meta:
        db_table = 'user_cards'
        app_label = 'models_app'
        verbose_name = 'Карточка пользователя'
        verbose_name_plural = 'Карточки пользователя'

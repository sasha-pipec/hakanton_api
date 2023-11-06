from django.db import models


class Event(models.Model):
    TYPE = (
        ('WithdrawBalance', 'Снять баланс'),
        ('TopUpBalance', 'Пополнить баланс'),
        ('Sleep', 'Заснуть'),
        ('Teleportation', 'Телепортация'),
    )
    title = models.CharField(max_length=255, verbose_name="Название события")
    types = models.CharField(
        max_length=15,
        choices=TYPE,
        default='WithdrawBalance',
        verbose_name='Тип события'
    )

    class Meta:
        db_table = 'events'
        app_label = 'models_app'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

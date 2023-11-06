from django.db import models


class Room(models.Model):
    WAITED = 'WAITED'
    STARTED = 'STARTED'

    STATUS = (
        (WAITED, 'В ожидании'),
        (STARTED, 'Запущена'),
    )
    users = models.ManyToManyField(to='User', blank=True, verbose_name='Игроки комнаты')
    status = models.CharField(max_length=7, choices=STATUS, default=WAITED, verbose_name='Статус')
    count_players = models.IntegerField(default=2, verbose_name='Кол-во игроков')

    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'rooms'
        app_label = 'models_app'
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

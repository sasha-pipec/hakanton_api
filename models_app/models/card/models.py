from django.db import models


class Card(models.Model):
    TOP = 'TOP'
    BOTTOM = 'BOTTOM'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    CORNER = 'CORNER'

    TYPE = (
        (TOP, 'Верх'),
        (BOTTOM, 'Низ'),
        (LEFT, 'Лево'),
        (RIGHT, 'Право'),
        (CORNER, 'Угол'),
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    cost = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(upload_to='cards/', verbose_name='Изображение')
    type = models.CharField(max_length=6, choices=TYPE, verbose_name='Тип')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cards'
        app_label = 'models_app'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

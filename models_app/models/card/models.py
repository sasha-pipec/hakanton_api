from django.db import models


class Card(models.Model):
    TOP = 'TOP'
    BOTTOM = 'BOTTOM'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    CORNER = 'CORNER'

    POSITIONS = (
        (TOP, 'Верх'),
        (BOTTOM, 'Низ'),
        (LEFT, 'Лево'),
        (RIGHT, 'Право'),
        (CORNER, 'Угол'),
    )

    DEFAULT = 'DEFAULT'
    EVENT = 'EVENT'

    TYPES = (
        (DEFAULT, 'Обычная'),
        (EVENT, 'Событие'),
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    cost = models.IntegerField(blank=True, null=True, verbose_name='Стоимость')
    image = models.ImageField(upload_to='cards/', verbose_name='Изображение')
    position = models.CharField(max_length=7, choices=POSITIONS, verbose_name='Позиция')
    type = models.CharField(max_length=7, choices=TYPES, verbose_name='Тип')
    index = models.IntegerField(default=0, verbose_name='Номер')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cards'
        app_label = 'models_app'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

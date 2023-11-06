from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class User(AbstractUser):
    """Overriding the User model with the email field as primary"""

    username = models.CharField(
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        }, verbose_name="Username",
        unique=True,
    )
    balance = models.IntegerField(default=16000, verbose_name='Баланс')
    color = models.CharField(max_length=7, verbose_name='Цвет')
    is_sleep = models.BooleanField(default=False, verbose_name='Состояние хода игрока')
    is_active = models.BooleanField(default=True, verbose_name='Состояние игрока')
    is_walk = models.BooleanField(default=False, verbose_name='Мой ход')
    position = models.IntegerField(default=0, verbose_name='Позиция')

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = 'models_app'
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

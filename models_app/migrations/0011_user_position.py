# Generated by Django 4.0 on 2023-11-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0010_alter_card_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.IntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
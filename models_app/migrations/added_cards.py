import os

from django.db import migrations
from rest_framework.utils import json

from models_app.models import Card

def added_cards(first_param, second_param):
    with open(os.path.join(os.path.dirname(__file__),
                           '..', '..', 'data', 'cards.json'),
              'r') as file:
        data = json.load(file)
        for item in data:
            Card.objects.create(
                title=item['Title'],
                cost=item['Cost'],
                position=item['type'],
                type=Card.DEFAULT
            )


class Migration(migrations.Migration):
    dependencies = [
        ('models_app', '0008_card_index'),
    ]
    operations = [
        migrations.RunPython(added_cards),
    ]

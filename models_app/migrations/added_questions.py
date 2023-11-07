import os

from django.db import migrations
from rest_framework.utils import json

from models_app.models import Question, Answer

def added_questions(first_param, second_param):
    with open(os.path.join(os.path.dirname(__file__),
                           '..', '..', 'data', 'questions.json'),
              'r', encoding="utf8") as file:
        data = json.load(file)
        for item in data:
            question = Question.objects.create(title=item['title'])
            for answer in item['answers']:
                Answer.objects.create(
                    title=answer['title'],
                    is_correct=answer['is_correct'],
                    question=question
                )


class Migration(migrations.Migration):
    dependencies = [
        ('models_app', '0008_card_index'),
    ]
    operations = [
        migrations.RunPython(added_questions),
    ]

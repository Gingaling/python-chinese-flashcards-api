# Generated by Django 4.1.3 on 2022-11-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_flashcard_pinyin_alter_flashcard_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='box',
            field=models.IntegerField(default=1),
        ),
    ]

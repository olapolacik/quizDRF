# Generated by Django 4.2.11 on 2024-04-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_answer_question_alter_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Quiz Title'),
        ),
    ]

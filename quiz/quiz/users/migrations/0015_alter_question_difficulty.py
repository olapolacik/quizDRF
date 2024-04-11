# Generated by Django 4.2.11 on 2024-04-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_question_technique_question_is_multiple_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Fundamental'), (2, 'Beginner'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Expert')], default=1, verbose_name='Difficulty'),
        ),
    ]

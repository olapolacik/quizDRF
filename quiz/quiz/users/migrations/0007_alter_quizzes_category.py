# Generated by Django 4.2.11 on 2024-04-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_answer_answer_text_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.category'),
        ),
    ]

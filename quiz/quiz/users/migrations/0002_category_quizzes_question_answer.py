# Generated by Django 4.2.11 on 2024-04-04 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('technique', models.IntegerField(choices=[(0, 'Multiple Choice')], default=0, verbose_name='Type of question')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('difficulty', models.IntegerField(choices=[(0, 'Fundamental'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0, verbose_name='Difficulty')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='users.quizzes')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='users.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]

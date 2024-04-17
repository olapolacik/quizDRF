import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from quiz.models import Category, Quizzes, Question, Answer


class Command(BaseCommand):
    help = "Seed the database with sample data"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of fake quizzes to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        seeder = Seed.seeder()

        seeder.add_entity(Category, 5)
        seeder.add_entity(Quizzes, total, {
            'title': lambda x: f"Quiz - {seeder.faker.word()}",
            'category': lambda x: random.choice(Category.objects.all())
        })

        for quiz in Quizzes.objects.all():
            for _ in range(5):
                question = seeder.faker.sentence()
                is_multiple = seeder.faker.boolean(chance_of_getting_true=50)

                question_obj = Question.objects.create(
                    quiz=quiz,
                    title=question,
                    is_multiple=is_multiple,
                    is_active=True
                )
                for _ in range(3):
                    answer_text = seeder.faker.word()
                    is_right = seeder.faker.boolean(chance_of_getting_true=30)

                    Answer.objects.create(
                        question=question_obj,
                        answer_text=answer_text,
                        is_right=is_right
                    )

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} quizzes with questions and answers.'))

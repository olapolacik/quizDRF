from django.core.management.base import BaseCommand
from faker import Faker
from quiz.users.models import Category, Quizzes, Question, Answer
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds the database with random data'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)
        parser.add_argument('--number', type=int, default=100)

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        number = kwargs['number']
        faker = Faker()

        # Tworzenie kategorii
        categories = ['Science', 'History', 'Geography', 'Literature', 'Sports']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        # Tworzenie quizów
        for _ in range(number):
            category = Category.objects.order_by('?').first()
            quiz = Quizzes.objects.create(
                title=faker.sentence(nb_words=4),
                category=category,
                date_created=timezone.now()
            )

            # Tworzenie pytań i odpowiedzi dla każdego quizu
            for _ in range(5):  # Tworzenie 5 pytań dla każdego quizu
                question = faker.sentence(nb_words=6)
                question_obj = Question.objects.create(
                    quiz=quiz,
                    title=question,
                    date_created=timezone.now(),
                    is_active=True,
                    is_multiple=False  # Zakładam, że pytania są jednokrotne
                )

                # Tworzenie odpowiedzi
                answers = [faker.word() for _ in range(3)]
                correct_answer = faker.random_element(answers)
                for answer_text in answers:
                    is_right = True if answer_text == correct_answer else False
                    Answer.objects.create(
                        question=question_obj,
                        answer_text=answer_text,
                        is_right=is_right
                    )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {number} records for {app_name}'))

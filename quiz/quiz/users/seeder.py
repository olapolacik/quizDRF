# Importy
from django_seed import Seed
from .models import Quizzes, Question, Answer, Category
import random

# Funkcja do generowania quizów
def generate_quizzes(seeder, number):
    seeder.add_entity(Quizzes, number, {
        'title': lambda x: seeder.faker.sentence(nb_words=4),
        'category': lambda x: Category.objects.get_or_create(name='Default Category')[0],
    })


# Funkcja do generowania pytań i odpowiedzi
def generate_questions(seeder, number):
    seeder.add_entity(Question, number, {
        'quiz': lambda x: random.choice(Quizzes.objects.all()),
        'title': lambda x: seeder.faker.sentence(nb_words=6),  # losowe zdanie składające się z 6 słów
        'difficulty': lambda x: random.randint(1, 5),
        'is_active': True,
        'is_multiple': lambda x: random.choice([True, False])
    })

    def _generate_answers_for_question(question):
        num_answers = 3
        num_correct_answers = 1
        if question.is_multiple:
            num_correct_answers = random.randint(1, num_answers)

        for _ in range(num_answers):
            is_right = num_correct_answers > 0
            seeder.add_entity(Answer, 1, {
                'question': question,
                'answer_text': lambda x: seeder.faker.sentence(nb_words=3),
                'is_right': is_right,
            })
            num_correct_answers -= 1

    questions = Question.objects.all()[:number]
    for question in questions:
        _generate_answers_for_question(question)


# Funkcja do generowania kategorii
def generate_categories(seeder):
    seeder.add_entity(Category, 1, {
        'name': lambda x: seeder.faker.sentence(nb_words=3)
    })

def generate_data(number):
    seeder = Seed.seeder()
    generate_categories(seeder)
    generate_quizzes(seeder, number)
    generate_questions(seeder, number * 5)
    inserted_pks = seeder.execute()
    
    print(inserted_pks)

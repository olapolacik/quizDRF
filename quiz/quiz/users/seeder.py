from django_seed import Seed
from .models import Quizzes, Question, Answer, Category
import random

# Funkcja do generowania quizow
def generate_quizzes(seeder, number):
    seeder.add_entity(Quizzes, number, {
        'title': lambda x: seeder.faker.sentence(nb_words=4),
        'category': lambda x: Category.objects.get_or_create(name='Default Category')[0],
    })


# Funkcja do generowania pytan
def generate_questions(seeder, number):
    seeder.add_entity(Question, number, {
        'quiz': lambda x: random.choice(Quizzes.objects.all()),
        'title': lambda x: seeder.faker.sentence(nb_words=6), # losowe zdanie skladajace sie z 6 slow
        'difficulty': lambda x: random.randint(1,5),
        'is_active': True,
        'is_multiple': lambda x: random.choice([True, False])
    })


# Funkcja do generowania odpowiedzi
def generate_answers(seeder, number):
    seeder.add_entity(Answer, number, {
        'question': lambda x: random.choice(Question.objects.all()),
        'answer_text': lambda x: seeder.faker.sentence(nb_words=3),
        'is_right': lambda x: random.choice([True, False]),
    })


# Funkcja do generowania kategori
def generate_categories(seeder):
    seeder.add_entity(Category, 1, {
        #'name': 'Default Category',
        'name': lambda x: seeder.faker.sentence(nb_words=3
        )
    })


# Funckja główna do generowania danych
def generate_data(number):
    seeder = Seed.seeder()
    generate_categories(seeder)
    generate_quizzes(seeder, number)
    generate_questions(seeder, number * 5)  
    generate_answers(seeder, number * 20)  
    inserted_pks = seeder.execute()

    print(inserted_pks)


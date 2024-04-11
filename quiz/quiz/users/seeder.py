# from django_seed import Seed
# from quizzes.models import Quizzes, Question, Answer, Category
# import random

# def generate_quizzes(seeder, number):
#     seeder.add_entity(Quizzes, number, {
#         'title': lambda x: seeder.faker.sentence(nb_words=4),
#         'category': lambda x: Category.objects.get_or_create(name='Default Category')[0],
#     })

# def generate_questions(seeder, number):
#     seeder.add_entity(Question, number, {
#         'quiz': lambda x: random.choice(Quizzes.objects.all()),
#         'technique': lambda x: random.randint(0, 0),  # assuming only one type of technique for now
#         'title': lambda x: seeder.faker.sentence(nb_words=6),
#         'difficulty': lambda x: random.randint(0, 4),
#         'is_active': True
#     })

# def generate_answers(seeder, number):
#     seeder.add_entity(Answer, number, {
#         'question': lambda x: random.choice(Question.objects.all()),
#         'answer_text': lambda x: seeder.faker.sentence(nb_words=3),
#         'is_right': lambda x: random.choice([True, False]),
#     })

# def generate_categories(seeder):
#     seeder.add_entity(Category, 1, {
#         'name': 'Default Category',
#     })

# def generate_data():
#     seeder = Seed.seeder()
#     generate_categories(seeder)
#     generate_quizzes(seeder, 10)
#     generate_questions(seeder, 50)
#     generate_answers(seeder, 200)
#     inserted_pks = seeder.execute()
#     print(inserted_pks)


# if __name__ == '__main__':
#     generate_data()

from django_seed import Seed
from .models import Quizzes, Question, Answer, Category
import random

def generate_quizzes(seeder, number):
    seeder.add_entity(Quizzes, number, {
        'title': lambda x: seeder.faker.sentence(nb_words=4),
        'category': lambda x: Category.objects.get_or_create(name='Default Category')[0],
    })

def generate_questions(seeder, number):
    seeder.add_entity(Question, number, {
        'quiz': lambda x: random.choice(Quizzes.objects.all()),
        'title': lambda x: seeder.faker.sentence(nb_words=6),
        'difficulty': lambda x: random.randint(1,5),
        'is_active': True,
        'is_multiple': lambda x: random.choice([True, False])
    })


def generate_answers(seeder, number):
    seeder.add_entity(Answer, number, {
        'question': lambda x: random.choice(Question.objects.all()),
        'answer_text': lambda x: seeder.faker.sentence(nb_words=3),
        'is_right': lambda x: random.choice([True, False]),
    })

def generate_categories(seeder):
    seeder.add_entity(Category, 1, {
        'name': 'Default Category',
    })

def generate_data(number):
    seeder = Seed.seeder()
    generate_categories(seeder)
    generate_quizzes(seeder, number)
    generate_questions(seeder, number * 5)  
    generate_answers(seeder, number * 20)  
    inserted_pks = seeder.execute()

    print(inserted_pks)


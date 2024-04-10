import random
from .models import Quizzes, Question, Answer, Category

def seed():
    # Pobiera istniejącą kategorię o id=1 lub tworzy nową
    category, created = Category.objects.get_or_create(id=1, defaults={'name': 'Default Category'})

    # Tworzy Quiz z tą kategorią
    quiz = Quizzes.objects.create(title="Quiz 1", category=category)

    for i in range(5):
        question = Question.objects.create(
            quiz=quiz,
            technique=random.choice([0]),
            title="Sample question",
            difficulty=random.choice([0, 1, 2, 3, 4]),
            is_active=True
        )

        Answer.objects.create(
            question=question,
            answer_text="Sample answer",
            is_right=random.choice([True, False])
        )

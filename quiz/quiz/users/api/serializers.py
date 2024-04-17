from rest_framework import serializers

from quiz.users.models import User, Quizzes, Answer, Question

# Serializator dla modelu User, wyświetla dane i url uzytkownika
class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }

# Serializator dla modelu Quizzes, wyświetla tytuł quizu
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            "title"
        ]

# Serializator dla modelu Answer, 
# wyświetla id, tekst odpowiedzi i info. czy odp jest poprawna
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "answer_text",
            "is_right"
        ]


# Serializator dla modelu Question, 
# wyświetla losowe pytanie z listą odpowiedzi
class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            "title",
            "answer"
        ]


# Serializator dla modelu Question, wyświetla pytanie, 
# listę odpowiedzi i przypisany quiz.
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            "quiz",
            "title",
            "answer"
        ]
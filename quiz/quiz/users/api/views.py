from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from quiz.users.models import Quizzes, Question, User

from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, RandomQuestionSerializer

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)



class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


class QuizWithQuestions(APIView):
    """
    Endpoint API zwracający quizy wraz z ich pytaniami.
    """
    def get(self, request, format=None):
        quizzes = Quizzes.objects.all()
        quiz_data = []

        for quiz in quizzes:
            quiz_serializer = QuizSerializer(quiz)
            quiz_questions = quiz.question.all()
            question_serializer = QuestionSerializer(quiz_questions, many=True)

            quiz_data.append({
                "quiz": quiz_serializer.data,
                "questions": question_serializer.data
            })

        return Response(quiz_data, status=status.HTTP_200_OK)
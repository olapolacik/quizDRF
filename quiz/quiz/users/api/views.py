from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Prefetch

from quiz.users.models import Quizzes, Question, User

from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, RandomQuestionSerializer, QuizCategorySerializer

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class QuizWithQuestions(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quizzes.objects.prefetch_related("questions").all()


class QuizCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        quizzes = Quizzes.objects.all()
        data = []

        for quiz in quizzes:
            serializer = QuizCategorySerializer(quiz)
            data.append(serializer.data)
        return Response(data, status=status.HTTP_200_OK)

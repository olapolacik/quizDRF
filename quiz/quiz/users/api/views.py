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


# API endpoint dla listy quizow
class Quiz(generics.ListAPIView):
    permission_classes = [AllowAny]

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()



# API endpoint dla losowego pytania
class RandomQuestion(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


# API endpoint dla pytan w danym quizie
class QuizQuestion(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


class QuizSearch(generics.ListAPIView):
    permission_classes = [AllowAny]

    serializer_class = QuizSerializer

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Quizzes.objects.all()

        #pobierz paramter wyszukiwania z URL
        name = self.request.query_params.get("name", None)
        category = self.request.query_params.get("category", None)
        difficulty = self.request.query_params.get("difficulty", None)

        if name:
            queryset = queryset.filter(title__icontains=name)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        return queryset
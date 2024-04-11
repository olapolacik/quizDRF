from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from quiz.users.api.views import Quiz, RandomQuestion, QuizQuestion, QuizSearch

app_name = "users"

urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
    path('quizzes/search/', QuizSearch.as_view(), name='quiz-search'),
]

#silk dodawania duzej ilosc rekordow do bazy
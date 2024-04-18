from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from quiz.users.api.views import Quiz, RandomQuestion, QuizQuestion, QuizWithQuestions

app_name = "users"

"""
Django runs through each URL pattern, in order,
and stops at the first one that matches the requested URL,
matching against path_info.
"""
urlpatterns = [
    path('quiz-with-questions/', QuizWithQuestions.as_view(), name='quiz-with-questions'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
]

# %20 to znak spacji w url np.
# path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
# to bedzie: http://localhost:8000/users/r/New%20Quiz/



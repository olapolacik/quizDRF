from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.db import models

class User(AbstractUser):
    """
    Default custom user model for quiz.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

# Model kategorii dla quizu
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Model reprezentujący quiz
class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))

    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model 
class Updated(models.Model):

    date_updated = models.DateTimeField(verbose_name=_("Last updated"), auto_now=True)

    class Meta:
        abstract = True

# Model reprezentujacy pytania
class Question(Updated):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE
    )

    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of question"))

    title = models.CharField(max_length=255, verbose_name=_("Title"))

    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))

    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Data Created"))

    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


# Model reprezentujacy odpowiedzi
class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
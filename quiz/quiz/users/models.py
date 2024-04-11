from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from asgiref.sync import sync_to_async
from django.db import models

class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]


    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})


# Model kategorii dla quizu

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class Quizzes(models.Model):
#     title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
#     category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = _("Quiz")
#         verbose_name_plural = _("Quizzes")
#         ordering = ['id']

#     def __str__(self):
#         return self.title
    
#     @staticmethod
#     def default_category():
#         default_category, created = Category.objects.get_or_create(
#             id=1, defaults={'name': 'Default Category'}
#         )
#         return default_category

  

class Quizzes(models.Model):

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    #category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)


    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    def __str__(self):
        return self.title

    @staticmethod
    def default_category():
        default_category, created = Category.objects.get_or_create(
            id=1, defaults={'name': 'Default Category'}
        )
        return default_category

class Updated(models.Model):

    date_updated = models.DateTimeField(verbose_name=_("Last updated"), auto_now=True)

    class Meta:
        abstract = True

# Model reprezentujacy pytania
class Question(Updated):

    SCALE = (
        (1, _('Fundamental')),
        (2, _('Beginner')),
        (3, _('Intermediate')),
        (4, _('Advanced')),
        (5, _('Expert'))
    )


    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, default=1, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))
    is_multiple = models.BooleanField(default=False, verbose_name=_("Multiple Answers"))

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']
  
# Model reprezentujacy odpowiedzi
class Answer(Updated):

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]
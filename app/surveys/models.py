from django.db import models
from django.contrib import admin


class SurveyQuestion(models.Model):
    question_title = models.CharField(max_length=50, blank=False)
    question_body = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.question_title


class SurveyAnswer(models.Model):
    question = models.ForeignKey(to=SurveyQuestion, on_delete=models.CASCADE)
    answer_title = models.CharField(max_length=50, blank=False)
    answer_choice = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.answer_title

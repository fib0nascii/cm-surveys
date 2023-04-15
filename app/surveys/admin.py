from django.contrib import admin
from .models import SurveyQuestion, SurveyAnswer


# Register your models here.
@admin.register(SurveyQuestion)
class SurveyQuestion(admin.ModelAdmin):
    pass


@admin.register(SurveyAnswer)
class SurveyAnswer(admin.ModelAdmin):
    pass

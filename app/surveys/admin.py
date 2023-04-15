from django.contrib import admin
from .models import SurveyQuestion


# Register your models here.
@admin.register(SurveyQuestion)
class SurveyQuestion(admin.ModelAdmin):
    pass

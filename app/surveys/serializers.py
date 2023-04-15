from rest_framework import serializers
from . import models


class SurveyQuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestion
        fields = ('id', 'question_title', 'question_body')


class SurveyQuestionAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyAnswer
        fields = ('id', 'question', 'answer_title', 'answer_choice')

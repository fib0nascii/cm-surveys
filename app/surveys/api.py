from rest_framework.viewsets import ModelViewSet
from .serializers import SurveyQuestionListSerializer, SurveyQuestionAnswerListSerializer
from . import models


class SurveyQuestionListViewSet(ModelViewSet):
    serializer_class = SurveyQuestionListSerializer

    def get_queryset(self):
        return models.SurveyQuestion.objects.all()


class SurveyQuestionAnswerListViewSet(ModelViewSet):
    serializer_class = SurveyQuestionAnswerListSerializer

    def get_queryset(self):
        return models.SurveyAnswer.objects.all()

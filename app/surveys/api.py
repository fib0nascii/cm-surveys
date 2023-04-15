from rest_framework.viewsets import ModelViewSet
from .serializers import SurveyQuestionListSerializer
from . import models


class SurveyQuestionListViewSet(ModelViewSet):
    serializer_class = SurveyQuestionListSerializer

    def get_queryset(self):
        return models.SurveyQuestion.objects.all()
from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register(r'questions', SurveyQuestionListViewSet, basename='survey-question-list')

urlpatterns = router.urls
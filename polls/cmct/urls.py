from django.conf.urls import url, include
from django.urls import path

from config.urls import router
from . import views

# app_name = 'cmct'
app_name = views.app_name

# rest_framework, url is like: http://localhost:8000/api/v1/cmct/question/
router.register(r'cmct/question', views.QuestionViewSet)
router.register(r'cmct/choice', views.ChoiceViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

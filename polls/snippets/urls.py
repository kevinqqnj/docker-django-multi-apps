from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from config.urls import router
from . import views

app_name = views.app_name

# rest_framework, url is like: http://localhost:8000/api/v1/cmct/question/
# router.register(r'cmct/question', views.QuestionViewSet)
# router.register(r'cmct/choice', views.ChoiceViewSet)

urlpatterns = [
    # url(r'^$', views.snippet_list),
    # url(r'^(?P<pk>[0-9]+)$', views.snippet_detail),
    path('', views.SnippetList.as_view(), name='index'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

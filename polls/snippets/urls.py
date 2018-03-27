from django.conf.urls import url, include
from django.urls import path

from config.urls import router
from . import views

app_name = views.app_name

# rest_framework, url is like: http://localhost:8000/api/v1/cmct/question/
# router.register(r'cmct/question', views.QuestionViewSet)
# router.register(r'cmct/choice', views.ChoiceViewSet)

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from config.urls import router
from . import views

app_name = views.app_name

router.register(r'snippets', views.SnippetViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

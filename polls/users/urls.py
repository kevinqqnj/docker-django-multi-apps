from django.conf.urls import url

from . import views
from config.urls import router

router.register(r'users', views.UserViewSet)
# router.register(r'users', views.UserList)
router.register(r'groups', views.GroupViewSet)

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]

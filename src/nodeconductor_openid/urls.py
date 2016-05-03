from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


def register_in(router):
    pass


urlpatterns = patterns('',
    url(r'^api-auth/openid/', include('django_openid_auth.urls'), name='auth-openid'),
)

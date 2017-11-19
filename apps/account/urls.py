from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^register/$', views.register, name='register'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
]

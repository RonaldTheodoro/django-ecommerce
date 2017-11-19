from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.ProductListView.as_view(), name='list'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.ProductListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='detail'),
]

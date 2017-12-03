from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.ProductListView.as_view(), name='list'),
    url(
        r'^(?P<slug>[\w-]+)$',
        views.ProductDetailView.as_view(),
        name='detail'
    ),
    url(
        r'^featured/list/$',
        views.ProductFeaturedListView.as_view(),
        name='featured_list'
    ),
    url(
        r'^featured/(?P<slug>[\w-]+)$',
        views.ProductFeaturedDetailView.as_view(),
        name='featured_detail'
    ),
]

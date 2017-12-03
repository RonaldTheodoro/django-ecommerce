from django.views import generic
from django.shortcuts import render, get_object_or_404

from . import models


class ProductListView(generic.ListView):
    queryset = models.Product.objects.all()
    template_name = 'product/list.html'


class ProductFeaturedListView(generic.ListView):
    template_name = 'product/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return models.Product.objects.all().filter(featured=True)


class ProductDetailView(generic.DetailView):
    queryset = models.Product.objects.all()
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        return super(ProductDetailView, self).get_context_data(*args, **kwargs)


class ProductFeaturedDetailView(generic.DetailView):
    template_name = 'product/detail.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return models.Product.objects.all()

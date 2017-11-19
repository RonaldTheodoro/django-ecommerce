from django.views import generic
from django.shortcuts import render, get_object_or_404

from . import models


class ProductListView(generic.ListView):
    queryset = models.Product.objects.all()
    template_name = 'product/list.html'


def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'product/list.html', {'product_list': products})


class ProductDetailView(generic.DetailView):
    queryset = models.Product.objects.all()
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        return super(ProductDetailView, self).get_context_data(*args, **kwargs)


def detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    return render(request, 'product/detail.html', {'product': product})

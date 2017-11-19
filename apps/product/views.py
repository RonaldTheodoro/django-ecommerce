from django.views import generic
from django.shortcuts import render

from . import models


class ProductListView(generic.ListView):
    queryset = models.Product.objects.all()
    template_name = 'product/list.html'


def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'product/list.html', {'product_list': products})

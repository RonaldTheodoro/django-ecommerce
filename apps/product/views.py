from django.views import generic
from django.shortcuts import render

from . import models


class ProductListView(generic.ListView):
    queryset = models.Product.objects.all()


def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

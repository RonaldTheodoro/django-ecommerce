from django.shortcuts import render

from . import forms


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    form = forms.ContactForm(request.POST or None)
    return render(request, 'core/contact.html', {'form': form})

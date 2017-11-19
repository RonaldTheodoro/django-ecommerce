from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import resolve

from . import forms


def sign_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = forms.LoginForm()

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            User = get_user_model()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username, email, password)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = forms.RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('/')

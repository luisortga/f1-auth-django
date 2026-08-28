from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render

from .forms import PilotForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()
                login(request, user)
                return redirect('pilots')
            except IntegrityError:  # noqa: E722
                return render(
                    request,
                    'signup.html',
                    {'form': UserCreationForm, 'error': 'Username already exists'},
                )

        return render(
            request,
            'signup.html',
            {'form': UserCreationForm, 'error': 'Password do not match'},
        )


def pilots(request):
    return render(request, 'pilots.html/')


def create_pilot(request):

    if request.method == 'GET':
        return render(request, 'create_pilot.html', {'form': PilotForm})
    else:
        form = PilotForm(request.POST)
        new_pilot = form.save(commit=False)
        new_pilot.user = request.user
        new_pilot.save()
        return redirect('pilots')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is None:
            return render(
                request,
                'signin.html',
                {
                    'form': AuthenticationForm,
                    'error': 'Username or Password is incorrect',
                },
            )
        else:
            login(request, user)
            return redirect('pilots')

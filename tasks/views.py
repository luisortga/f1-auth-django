from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PilotForm
from .models import Pilot

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(
            request,
            'signup.html',
            {'form': UserCreationForm},
        )

    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )

            user.save()
            login(request, user)

            return redirect('pilots')

        except IntegrityError:
            return render(
                request,
                'signup.html',
                {
                    'form': UserCreationForm,
                    'error': 'Username already exists',
                },
            )

    return render(
        request,
        'signup.html',
        {
            'form': UserCreationForm,
            'error': 'Password do not match',
        },
    )


@login_required
def pilots(request: HttpRequest) -> HttpResponse:

    pilots_all = Pilot.objects.filter(user=request.user)

    return render(request, 'pilots.html', {'pilots_all': pilots_all})


@login_required
def create_pilot(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(
            request,
            'create_pilot.html',
            {'form': PilotForm},
        )

    form = PilotForm(request.POST)

    if form.is_valid():
        new_pilot = form.save(commit=False)
        new_pilot.user = request.user
        new_pilot.save()

        return redirect('pilots')
    else:
        return render(
            request,
            'create_pilot.html',
            {'form': PilotForm, 'error': 'Please provide valida data'},
        )


@login_required
def delete_pilot(request: HttpRequest, pilot_id: int):
    pilot = get_object_or_404(Pilot, pk=pilot_id, user=request.user)
    if request.method == 'POST':
        pilot.delete()
        return redirect('pilots')


@login_required
def pilot_detail(request: HttpRequest, pilot_id: int) -> HttpResponse:
    if request.method == 'GET':
        pilot = get_object_or_404(Pilot, pk=pilot_id, user=request.user)
        form = PilotForm(instance=pilot)
        return render(request, 'pilot_detail.html', {'pilot': pilot, 'form': form})
    else:
        try:
            pilot = get_object_or_404(Pilot, pk=pilot_id, user=request.user)
            form = PilotForm(request.POST, instance=pilot)
            form.save()
            return redirect('pilots')
        except ValueError:
            return render(
                request,
                'pilot_detail.html',
                {'pilot': pilot, 'form': form, 'error': 'Error updating pilot'},
            )


@login_required
def signout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')


def signin(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(
            request,
            'signin.html',
            {'form': AuthenticationForm},
        )

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

    login(request, user)

    return redirect('pilots')

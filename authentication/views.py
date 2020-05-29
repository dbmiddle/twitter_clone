from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from authentication.forms import LoginForm
from authentication.forms import SignupForm
from twitteruser.models import MyUser

# Create your views here.


def loginview(request):
    html = 'loginform.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutview(request):
    if request.method == 'GET':
        logout(request)

    return HttpResponseRedirect(reverse('homepage'))


def signup(request):
    html = 'signup_form.html'

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                data['user_name'], data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, html, {'form': form})

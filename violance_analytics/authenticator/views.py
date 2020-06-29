from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('contact')
    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is created for '+ user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('contact')
    else:
        context = {}
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contact')
            else:
                messages.info(request, 'Username or password is incorrect.')

        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



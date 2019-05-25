from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """ Return the index.html file """
    return render(request, 'index.html')

@login_required   
def logout(request):
    """ log the user out """
    auth.logout(request)
    messages.success(request, 'You have loged out!')
    return redirect(reverse('index'))
    
def login(request):
    """ Return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have sucessfully loged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form' : login_form})
    
def register(request):
    """ Registre Account page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registred')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to register your account at this time')
    else:
        register_form = UserRegisterForm()
    return render(request, 'register.html', {"register_form" : register_form})
    
def user_profile(request):
    """ User profile page """
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile' : user})
from django.shortcuts import render,redirect
from .forms import Register #, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
    

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Register(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                return redirect('signin')
        else:
            form = Register()
        return render(request, 'signup.html', {'form':form})
    else:
        return redirect('profile')

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
    else:
        return redirect('profile')

    
@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('signin')

@login_required
def change_pass(request):
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Updated!')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})

@login_required
def new_pass(request):
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'New Password added!')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})

from django.shortcuts import render,redirect
from .forms import Register, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from blogs.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data':data})
    
@login_required
def update_profile(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Updated successfully')
                return redirect('signin')
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'update_profile.html', {'form':form})
    # else:
    #     return redirect('signin')


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

# def signin(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request,data = request.POST)
#             if form.is_valid():
#                 name = form.cleaned_data['username']
#                 userpass = form.cleaned_data['password']
#                 user = authenticate(username=name, password=userpass)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('profile')
#         else:
#             form = AuthenticationForm()
#         return render(request, 'signin.html', {'form':form})
#     else:
#         return redirect('profile')

class SignIn(LoginView):
    template_name = 'signin.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Loggedin Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


    
@login_required
def signout(request):
    logout(request)
    return redirect('signin')

class SignOut(LogoutView):
    def get_success_url(self):
        return reverse_lazy('blog')

@login_required
def change_pass(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    # else:
    #     return redirect('signin')

@login_required
def new_pass(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    # else:
    #     return redirect('signin')






#--------------------------------------------------------------------
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect(add_author)
#     else:
#         author_form = AuthorForm()
#     return render(request, 'add_author.html', {'form':author_form})

# # Create your views here.
# def add_profile(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect(add_profile)
#     else:
#         profile_form = ProfileForm()
#     return render(request, 'add_profile.html', {'form':profile_form})


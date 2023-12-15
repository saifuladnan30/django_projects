
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('new_pass/', views.new_pass, name='new_pass'),
    path('profile/', views.profile, name='profile'),
]
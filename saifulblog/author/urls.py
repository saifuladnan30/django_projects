
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    # path('signout/', views.signout, name='signout'),
    path('signout/', views.SignOut.as_view(), name='signout'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('new_pass/', views.new_pass, name='new_pass'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.update_profile, name='edit_profile'),
    # path('add_author/', views.add_author, name='add_author'),
    # path('add_profile/', views.add_profile, name="add_profile")
]

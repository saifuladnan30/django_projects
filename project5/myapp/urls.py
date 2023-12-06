
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('htmlform/', views.htmlform, name='htmlform'),
    path('django_form/', views.djangoForm, name='django_form'),
    path('student_form/', views.studentForm, name='student_form'),
    path('password_validation/', views.PasswordValidation, name='password_validation'),
]

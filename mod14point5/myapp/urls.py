
from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_form, name='form'),
    path('model/', views.modelForm, name='model_form'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog),
    path('', views.home)
]

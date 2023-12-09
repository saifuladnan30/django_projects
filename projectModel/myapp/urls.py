
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detele/<int:roll>', views.deleteStudent, name='delete_student'),
]

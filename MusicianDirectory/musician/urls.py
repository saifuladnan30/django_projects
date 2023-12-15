
from django.urls import path
from .views import AddMusician

urlpatterns = [
    path('add/', AddMusician.as_view(), name="add_musician"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('authors/', include('authors.urls')),
    path('categories/', include('categories.urls')),
    path('profiles/', include('profiles.urls')),
]

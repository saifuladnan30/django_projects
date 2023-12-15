
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('album.urls')),
    path('musician/', include('musician.urls')),
]

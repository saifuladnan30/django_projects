
from django.urls import path
from .views import AlbumList, AddAlbum, EditAlbum, DeleteAlbum

urlpatterns = [
    path('', AlbumList.as_view(), name="album"),
    path('add/', AddAlbum.as_view(), name="add_album"),
    path('edit/<int:pk>', EditAlbum.as_view(), name="edit_album"),
    path('delete/<int:pk>', DeleteAlbum.as_view(), name="delete_album"),
]

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Album
from musician.models import Musician
from .forms import AlbumForm

class AlbumList(ListView):
    model = Musician
    template_name = 'album.html'
    context_object_name = 'data'

class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('album')

class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('album')

class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('album')
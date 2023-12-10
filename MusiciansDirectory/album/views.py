from django.shortcuts import render, redirect
from . import forms
from .models import Album
from musician.models import Musician
# Create your views here.
def album(request):
    # data = Album.objects.all()
    data = Musician.objects.all()
    return render(request, 'album.html', {'data':data})


# add
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form':album_form})

# edit
def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    
    return render(request, 'add_album.html', {'form':album_form})

# delete
def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('album')
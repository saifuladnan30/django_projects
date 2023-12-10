from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
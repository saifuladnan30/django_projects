
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import MusicianForm

class AddMusician(CreateView):
    template_name = 'add_musician.html'
    form_class = MusicianForm
    success_url = reverse_lazy('add_musician')

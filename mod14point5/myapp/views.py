from django.shortcuts import render, redirect
from .forms import PracticeForm, Model_Form

# Create your views here.
def django_form(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('form')
    else:
        form = PracticeForm()
    return render(request, 'form.html', {'form':form})

def modelForm(request):
    if request.method == 'POST':
        form = Model_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_form')
    else:
        form = Model_Form()
    return render(request, 'model_form.html', {'form':form})
from django.shortcuts import render, redirect
from . import forms
from .models import Task
# Create your views here.
def task(request):
    data = Task.objects.all()
    return render(request, 'task.html', {'data':data})


# add
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect(task)
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form':task_form})

# edit
def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task')
    
    return render(request, 'add_task.html', {'form':task_form})

# delete
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('task')
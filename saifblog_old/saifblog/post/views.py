from django.shortcuts import render, redirect
from . import forms
from .models import Post
# Create your views here.
def blog(request):
    data = Post.objects.all()
    print(data)
    return render(request, 'blog.html', {'data':data})


# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect(add_post)
    else:
        post_form = forms.PostForm()
    return render(request, 'post.html', {'form':post_form})

# edit posts here
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect(blog)
    
    return render(request, 'post.html', {'form':post_form})

# delete posts here
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect(blog)
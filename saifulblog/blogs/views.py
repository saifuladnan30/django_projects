from django.shortcuts import render, redirect
from . import forms
from . import models
from .forms import PostForm
from categories.models import Category
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy


# Create your views here.
def blog(request, category_slug=None):
    data = models.Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = models.Post.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request, 'blog.html', {'data':data, 'category':categories})

# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST)
#         if post_form.is_valid():
#             # Set the author field to the current user before saving
#             post_instance = post_form.save(commit=False)
#             post_instance.author = request.user
#             post_instance.save()
#             post_form.save_m2m()  # Save the ManyToMany relationships, including categories
#             return redirect('blog')  # Assuming 'add_post' is the name of your view
#     else:
#         post_form = forms.PostForm()
#     return render(request, 'post.html', {'form': post_form})


# @login_required
class AddPost(CreateView):
    model = models.Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# edit posts here
# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     post_form = forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form = forms.PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect(blog)
#     return render(request, 'post.html', {'form':post_form})

@method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

# delete posts here
@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect(blog)


class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete_confirm.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

class PostDetails(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentsForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return redirect('post_details', id=post.id)

        # If the form is not valid, you may want to handle this case differently.
        # For example, you could render the same page with an error message.

        # Assuming you have a 'post-details' URL pattern for this view:
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentsForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
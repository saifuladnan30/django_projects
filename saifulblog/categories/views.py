from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

# Create your views here.

@login_required
def add_categories(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.slug = slugify(category.cat_name)
            category.save()
            return redirect(add_categories)
    else:
        category_form = forms.CategoryForm()
    return render(request, 'category.html', {'form': category_form})

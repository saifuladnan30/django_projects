from django.shortcuts import render

def blog(request):
    return render(request,'homepage/blog.html')

def home(request):
    return render(request, 'homepage/index.html')
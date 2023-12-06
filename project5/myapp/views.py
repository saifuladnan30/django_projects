from django.shortcuts import render
from . forms import contactForm, studentData, passwordValidation

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        country = request.POST.get('country')
        return render(request, 'about.html', {'name':name, 'email':email, 'country':country})
    else:
        return render(request, 'about.html')
def htmlform(request):
        return render(request, 'htmlform.html')
def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./myapp/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'django_form.html', {'form':form})
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form':form})


def studentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'django_form.html', {'form':form})
    else:
        form = studentData()
    return render(request, 'django_form.html', {'form':form})

def PasswordValidation(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'django_form.html', {'form':form})
    else:
        form = passwordValidation()
    return render(request, 'django_form.html', {'form':form})
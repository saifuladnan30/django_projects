from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class Register(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ChangeUserData(UserChangeForm):
    password = None #for not showing password field in form
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

#--------------------------------------------------------
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
from django import forms
from . models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

        labels = {
            'name' : 'Student Name',
            'roll' : 'ID'
        }
        widgets = {
            'address' : forms.TextInput(attrs={'class' : 'bg-light text-dark'})
        }
        error_messages = {
            'name' : {'required' : 'Name required'}
        }
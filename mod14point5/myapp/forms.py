from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import PracticeModelForm

class Model_Form(forms.ModelForm):
    class Meta:
        model = PracticeModelForm
        fields = '__all__'

        
class PracticeForm(forms.Form):
    name = forms.CharField(max_length=50,initial='Your name')
    email = forms.EmailField(label="Please enter your email address",)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)


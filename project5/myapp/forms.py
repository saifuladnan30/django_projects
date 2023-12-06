from typing import Any
from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(initial="Adnan", help_text="Enter your full name", required=False, widget=forms.Textarea(attrs={'id':'text_area', 'placeholder': 'enter your name'}))
    # file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    exam = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # select = forms.MultipleChoiceField()
    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,required=False, widget=forms.RadioSelect)
    size2 = forms.MultipleChoiceField(choices=CHOICES,required=False, widget=forms.CheckboxSelectMultiple)


# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter your name than 10 character!')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain '.com'")
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter your name than 10 character!')
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain '.com'")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("enter at least 10 character")
    
class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter your name than 10 character!')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid Email")])
    text= forms.CharField(required=False,widget=forms.TextInput, validators=[len_check])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18, message="you should at least 18 years old"),validators.MaxValueValidator(34, message="you should max 34 years old")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message="only pdf and png is allowed")])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        if len(val_name) < 6:
            raise forms.ValidationError("Name must be at least 6 character")
        if val_con_pass != val_pass:
            raise forms.ValidationError("Password don't match")
        elif len(val_pass) < 8:
            raise forms.ValidationError("Password must be at least 8 character")
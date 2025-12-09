from django import forms
from .models import UserRequirement
from django.contrib.auth.forms import UserCreationForm

class FormR(UserCreationForm):
    class Meta:
        model = UserRequirement
        fields = ['Reg_Number','first_name','last_name', 'department', 'level', 'email', 'phone_number', 'password1', 'password2']
        widgets = {
            'Reg_Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example : 224008135'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'olivier@gmail.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+250788123456'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Reg_Number'].help_text = "Required. 9 characters."
           
        def clean_reg_number(self):
            reg_number = self.cleaned_data.get('Reg_Number')
            if UserRequirement.objects.filter(Reg_Number=reg_number).exists():
                raise forms.ValidationError("Registration number already exists.")
            return reg_number

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = UserRequirement
        fields = ['Reg_Number', 'password']
        Reg_Number = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g:224008135'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
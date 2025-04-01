from django import forms
from django.contrib.auth.models import User
from .models import LoanAccount

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")  # Changed 'name' to 'username'
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanAccount
        fields = ['name', 'surname', 'dob', 'address', 'reason', 'loan_type', 'amount', 'interest_rate']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})  # Fixed syntax
        }

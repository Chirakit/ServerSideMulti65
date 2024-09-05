from datetime import datetime

from django import forms

from .models import Position

GENDER_CHOICES = (
    ("Choose", '---------'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('LGBT', 'Other')
)


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=GENDER_CHOICES,
        required=True
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        initial=datetime.today()
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        initial=datetime.today()
    )
    salary = forms.DecimalField(
        widget=forms.NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
        initial=0
    )
    position = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Position.objects.all(),
        required=True
    )

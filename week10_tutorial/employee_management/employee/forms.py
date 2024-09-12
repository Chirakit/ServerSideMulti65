from django import forms
from .models import Position
from datetime import datetime

class EmployeeForm(forms.Form):
    gender_choice = (
        ("M", "M"),
        ("F", "F"),
        ("LGBT", "LGBT"),
    )

    first_name = forms.CharField(label="First name:", max_length=100)
    last_name = forms.CharField(label="Last name:", max_length=100)
    gender = forms.ChoiceField(label="Gender:", choices=gender_choice, required=True)
    birth_date = forms.DateField(label="Birth date:",
                                widget=forms.DateInput(attrs={"type" :"date"}))
    hire_date = forms.DateField(label="Hire date:",
                               widget=forms.DateInput(attrs={"type" :"date"}))
    salary = forms.IntegerField(label="Salary:", required=True)
    position = forms.ModelChoiceField(
        queryset = Position.objects.all()
    )
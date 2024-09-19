from datetime import date
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Employee, EmployeeAddress, Project

class EmployeeForm(ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={"cols": 30, "rows": 3}))
    district = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=15)

    class Meta:
        model = Employee
        fields = [
            "first_name", 
            "last_name", 
            "gender", 
            "birth_date", 
            "hire_date", 
            "salary", 
            # "position",
            "location",
            "district",
            "province",
            "postal_code"
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hire_date = cleaned_data.get("hire_date")
        if date.today() < hire_date:
            self.add_error(
                'hire_date',
                'Hire date should not be future'
            )
        return cleaned_data

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "due_date",
            "start_date",
            "description",
            "manager",
            "staff"
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'staff': forms.SelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        if due_date < start_date:
            self.add_error(
                'start_date',
                'Start date should not be before Due date'
            )
        return cleaned_data

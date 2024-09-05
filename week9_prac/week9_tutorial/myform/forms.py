from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="My name", max_length=100)
    email = forms.EmailField(label="My email", required=False)
    bio = forms.CharField(label="My bio", widget=forms.Textarea(
        attrs={"rows": 3, "cols": 20}
    ))
    birthdate = forms.DateField(label="My birthdate", widget=forms.SelectDateWidget)
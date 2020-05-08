from django import forms


class CreateForm(forms.Form):
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password_again = forms.CharField(max_length=100)
    mail = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)



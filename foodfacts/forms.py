from django import forms


class NavSearchForm(forms.Form):
    nav_search = forms.CharField(max_length=100)

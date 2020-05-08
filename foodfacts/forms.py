from django import forms


class NavSearchForm(forms.Form):
    nav_search = forms.CharField(max_length=100)

    def get_search_term(self):
        search_term = self.data.get("nav_search", "empty")
        if search_term == "":
            return "empty"
        else:
            return search_term

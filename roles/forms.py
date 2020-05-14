from django import forms
from django.core.exceptions import ValidationError


class CreateForm(forms.Form):
    Prenom = forms.CharField(max_length=100)
    Nom = forms.CharField(max_length=100)
    Mot_De_Passe = forms.CharField(max_length=100)
    Repeter_Mot_De_Passe = forms.CharField(max_length=100)
    Mail = forms.CharField(max_length=100)
    Telephone = forms.CharField(max_length=100)

    def is_valid(self):
        if self.data.get("Mot_De_Passe") != self.data.get("Repeter_Mot_De_Passe"):
            self.add_error(field="Mot_De_Passe",
                           error=ValidationError("Les deux mots de passe sont doivent être identiques", code="unmatch"))
            super()
            return False
        else:
            super()
            return True

    def get_first_name(self):
        return self.data.get("Prenom", "empty")

    def get_last_name(self):
        return self.data.get("Nom", "empty")

    def get_password(self):
        return self.data.get("Mot_De_Passe", "empty")

    def get_password_again(self):
        return self.data.get("Repeter_Mot_De_Passe", "empty")

    def get_phone(self):
        return self.data.get("Telephone", "empty")

    def get_mail(self):
        return self.data.get("Mail", "empty")


class SigninForm(forms.Form):
    signin_email = forms.CharField(max_length=100)
    signin_password = forms.CharField(max_length=100)

    def get_mail(self):
        return self.data.get("signin_email", "empty")

    def get_password(self):
        return self.data.get("signin_password", "empty")


class UpdateProfileForm(forms.Form):
    update_email = forms.CharField(max_length=100)
    update_first_name = forms.CharField(max_length=100)
    update_last_name = forms.CharField(max_length=100)
    confirm_email = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

    def get_update_email(self):
        return self.data.get("update_email", "empty")

    def get_update_first_name(self):
        return self.data.get("update_first_name", "empty")

    def get_update_last_name(self):
        return self.data.get("update_last_name", "empty")

    def get_confirm_email(self):
        return self.data.get("confirm_email", "empty")

    def get_confirm_password(self):
        return self.data.get("confirm_password", "empty")


class LikeForm(forms.Form):
    liked_id = forms.IntegerField()
    replaced_id = forms.CharField(max_length=100)
    replaced_name = forms.CharField(max_length=100)
    replaced_nutrigrade = forms.CharField(max_length=100)
    userid = forms.CharField(max_length=100)

    def get_liked_id(self):
        return self.data.get("liked_id", "empty")

    def get_replaced_id(self):
        return self.data.get("replaced_id", "empty")

    def get_replaced_name(self):
        return self.data.get("replaced_name", "empty")

    def get_replaced_nutrigrade(self):
        return self.data.get("replaced_nutrigrade", "empty")

    def get_user_id(self):
        return self.data.get("userid", "empty")


class UnlikeForm(forms.Form):
    unliked_id = forms.IntegerField()
    userid_unlike = forms.CharField(max_length=100)

    def get_unliked_id(self):
        return self.data.get("unliked_id", "empty")

    def get_userid_unlike(self):
        return self.data.get("userid_unlike", "empty")

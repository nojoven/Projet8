from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import CreateForm, SigninForm, UpdateProfileForm
from django.contrib.auth.models import User, AbstractBaseUser, UserManager
from django.contrib.auth import authenticate, login, logout
from . import EmailBackend
import foodfacts.models as models


def create_user(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        print(form)
        if form.is_valid():
            user_first_name = form.get_first_name()
            user_last_name = form.get_last_name()
            user_phone = form.get_phone()
            user_phone_ending = user_phone[-6:-1]
            username = f"{user_first_name}{user_phone_ending}{user_last_name}"
            password = form.get_password()
            mail = form.get_mail()
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=mail,
                                            first_name=user_first_name,
                                            last_name=user_last_name
                                            )
            user.save()
            login(request, user)
            return HttpResponseRedirect('/foodfacts/account')

        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': CreateForm()})


def signin_user(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        user = authenticate(request, username=form.get_mail(), password=form.get_password())

        if user is not None:
            login(request, user)
            return render(request, 'mon_compte.html')
        else:
            form.add_error(field="signin_email", error=ValidationError("Email incorrect", code="signin_mail"))
            form.add_error(field="signin_password", error=ValidationError("Mot de passe incorrect", code="signin_password"))
            return render(request, "signin.html", {'form': form})

    return render(request, "signin.html", {'form': SigninForm()})


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        update_first_name = form.get_update_first_name()
        update_last_name = form.get_update_last_name()
        update_email = form.get_update_email()
        confirm_email = form.get_confirm_email()
        confirm_email_password = form.get_confirm_password()

        if update_first_name or update_last_name or update_email:
            user = authenticate(username=confirm_email, password=confirm_email_password)
            if user is not None:
                if update_email != "":
                    user.email = update_email
                if update_first_name != "":
                    user.first_name = update_first_name
                if update_last_name != "":
                    user.last_name = update_last_name
                user.save()
                return render(request, 'mon_compte.html', {"user": user})
            else:
                form.add_error(field="confirm_email",
                               error=ValidationError("Email de confirmation incorrect", code="confirm_email"))
                form.add_error(field="confirm_password",
                               error=ValidationError("Mot de passe de confirmation incorrect", code="confirm_email"))
                return render(request, "mon_compte.html", {'form': form})

        return render(request, "mon_compte.html", {'form': form})

    return render(request, "mon_compte.html", {'form': UpdateProfileForm()})

def logout_user(request):
    logout(request)
    return render(request, "signin.html")

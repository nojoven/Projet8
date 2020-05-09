from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import CreateForm, SigninForm
from django.contrib.auth.models import User, AbstractBaseUser, UserManager
from django.contrib.auth import authenticate
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
            return HttpResponseRedirect('/foodfacts/account')

        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': CreateForm()})


def signin_user(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        user = authenticate(username=form.get_mail(), password=form.get_password())

        if user is not None:
            return render(request, 'mon_compte.html', {"user": user})
        else:
            form.add_error(field="signin_email", error=ValidationError("Email incorrect", code="signin_mail"))
            form.add_error(field="signin_password", error=ValidationError("Mot de passe incorrect", code="signin_password"))
            return render(request, "signin.html", {'form': form})

    return render(request, "signin.html", {'form': SigninForm()})



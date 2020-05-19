from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CreateForm, SigninForm, UpdateProfileForm, LikeForm, UnlikeForm
from foodfacts.modules.database_service import DatabaseService
from django.contrib.auth import login, logout
import foodfacts.models as models


def create_user(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        user = None
        if form.is_valid():
            user_first_name = form.cleaned_data["Prenom"]
            user_last_name = form.cleaned_data["Nom"]
            user_phone = form.cleaned_data["Telephone"]
            user_phone_ending = user_phone[-6:-1]
            username = f"{user_first_name}{user_phone_ending}{user_last_name}"
            password = form.cleaned_data["Mot_De_Passe"]
            mail = form.cleaned_data["Mail"]
            user = DatabaseService.create_user(username, password, mail, user_first_name, user_last_name)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/roles/account')
            else:
                return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': CreateForm()})


def signin_user(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        user = None
        if form.is_valid():
            provided_mail = form.cleaned_data["signin_email"]
            provided_password = form.cleaned_data["signin_password"]
            user = DatabaseService.identify(request, provided_mail, provided_password)

        if user is not None:
            login(request, user)
            return render(request, 'mon_compte.html')
        else:
            form.add_error(field="signin_email", error=ValidationError("Email incorrect", code="signin_mail"))
            form.add_error(field="signin_password", error=ValidationError("Mot de passe incorrect",
                                                                          code="signin_password"))
            return render(request, "signin.html", {'form': form})

    return render(request, "signin.html", {'form': SigninForm()})


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        user = None
        if form.is_valid():
            update_first_name = form.cleaned_data["update_first_name"]
            update_last_name = form.cleaned_data["update_last_name"]
            update_email = form.cleaned_data["update_email"]
            confirm_email = form.cleaned_data["confirm_email"]
            confirm_password = form.cleaned_data["confirm_password"]
        else:
            return render(request, "mon_compte.html", {'form': form})

        if update_first_name or update_last_name or update_email:
            user = DatabaseService.identify(request, confirm_email, confirm_password)
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
        else:
            return render(request, "mon_compte.html", {'form': form})

    return render(request, "mon_compte.html", {'form': UpdateProfileForm()})


def logout_user(request):
    logout(request)
    return render(request, "signin.html")


def like(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            liked_id = form.cleaned_data["liked_id"]
            replaced_id = form.cleaned_data["replaced_id"]
            replaced_name = form.cleaned_data["replaced_name"]
            replaced_nutrigrade = form.cleaned_data["replaced_nutrigrade"]
            userid = form.cleaned_data["userid"]

            if liked_id:
                product = DatabaseService.select_liked_in_products(liked_id)

                like_data = dict()
                like_data["productid"] = liked_id
                like_data["name"] = product.productname
                like_data["nutrigrade"] = product.nutrigrade
                like_data["stores"] = product.stores
                like_data["brands"] = product.brands
                like_data["category"] = product.category
                like_data["quantity"] = product.quantity
                like_data["replacedid"] = replaced_id
                like_data["replacedarticle"] = replaced_name
                like_data["replacednutrigrade"] = replaced_nutrigrade
                like_data["userid"] = userid
                like_data["front_img"] = product.front_img

                if not models.Favorites.objects.filter(productid=product.idproduct).exists():
                    query = models.Favorites(**like_data)
                    query.save()
            url = reverse("search_term", args=[replaced_name])
            return HttpResponseRedirect(url)
        else:
            return render(request, "resultats.html", {'form': form})
    else:
        return render(request, "resultats.html")


def favourites(request):
    userid = request.user.id
    user_favs = DatabaseService.select_user_favs(userid)
    return render(request, "mes_aliments.html", {"favlist": user_favs})


def unlike(request):
    if request.method == 'POST':
        form = UnlikeForm(request.POST)
        if form.is_valid():
            unliked_id = form.cleaned_data["unliked_id"]
            userid_unlike = form.cleaned_data["userid_unlike"]
            DatabaseService.remove_user_fav(userid_unlike, unliked_id)

        url = reverse("favourites")
        return HttpResponseRedirect(url)


def register(request):
    return render(request, "register.html")


def account(request):
    return render(request, "mon_compte.html")

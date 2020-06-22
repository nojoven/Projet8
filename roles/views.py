import logging
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # changer noms inputs
# django form.as_p() dans mon formulaire
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import foodfacts.models as models
from random import randrange as ra
from .forms import (
    # CreateForm,
    SigninForm,
    UpdateProfileForm,
    LikeForm,
    UnlikeForm
)

LOGGER = logging.getLogger(__name__)


def create_user(request):
    """Creates a user based on form inputs"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request)
        if form.is_valid():
            print("YEEEEES")
            form.save()
            # form.username, password
            # login avec username et password
            # return HttpResponseRedirect("/roles/account")
            return HttpResponseRedirect("/roles/signin")
        else:
            return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": UserCreationForm()})


def signin_user(request):
    """Logs a user in based on form inputs"""
    if request.method == "POST":
        form = SigninForm(request.POST)
        user = None
        if form.is_valid():
            provided_mail = form.cleaned_data["email"]
            provided_password = form.cleaned_data["password"]
            user = authenticate(
                request,
                username=provided_mail,
                password=provided_password
                )

            if user is not None:
                login(request, user)
                return render(request, "mon_compte.html")
            else:
                form.add_error(
                        field="email",
                        error=ValidationError("Email ou mot de passe incorrect"),
                    )
                return render(request, "signin.html", {"form": form})

        else:
            # traiter les pb de longueur ou d'invalidité dans forms.py
            return render(request, "signin.html", {"form": form})

    return render(request, "signin.html", {"form": SigninForm()})


def update_profile(request):
    """Updates user data based on user inputs."""
    if request.method == "POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            update_first_name = form.cleaned_data["update_first_name"]
            update_last_name = form.cleaned_data["update_last_name"]
            update_email = form.cleaned_data["update_email"]
            confirm_email = form.cleaned_data["confirm_email"]
            confirm_password = form.cleaned_data["confirm_password"]
        else:
            return render(request, "mon_compte.html", {"form": form})

        if update_first_name \
                or update_last_name \
                or update_email:
            user = authenticate(
                request,
                username=confirm_email,
                password=confirm_password
                )

            if user is not None:
                if update_email != "":
                    user.email = update_email
                if update_first_name != "":
                    user.first_name = update_first_name
                if update_last_name != "":
                    user.last_name = update_last_name
                user.save()
                return render(request, "mon_compte.html", {"user": user})
            else:
                form.add_error(
                    field="confirm_email",
                    error=ValidationError(
                        "Email de confirmation incorrect",
                        code="confirm_email"
                    ),
                )
                form.add_error(
                    field="confirm_password",
                    error=ValidationError(
                        "Mot de passe à bien confirmer.",
                        code="confirm_email"
                    ),
                )
                return render(request, "mon_compte.html", {"form": form})
        else:
            return render(request, "mon_compte.html", {"form": form})

    return render(request, "mon_compte.html", {"form": UpdateProfileForm()})


def logout_user(request):
    """Logs out a user based on form inputs"""
    logout(request)
    return render(request, "signin.html")


def like(request, product_id, replaced_id):
    """Adds a favourite to the database for a user"""
    if request.method == "POST":
        LOGGER.info("LIKE FORM")
        user = request.user

        if product_id:
            product = select_liked_in_products(product_id)

            like_data = dict()
            like_data["productid"] = product_id
            like_data["name"] = product.productname
            like_data["nutrigrade"] = product.nutrigrade
            like_data["stores"] = product.stores
            like_data["brands"] = product.brands
            like_data["category"] = product.category
            like_data["quantity"] = product.quantity
            like_data["replacedid"] = replaced_id
            like_data["userid"] = user.id
            like_data["front_img"] = product.front_img

            if not models.Favorites.objects.filter(
                productid=product.idproduct
            ).exists():
                query = models.Favorites(**like_data)
                query.save()
            # url = reverse("search_term", args=[replaced_name])
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            return render(request, "resultats.html")
    else:
        return render(request, "resultats.html")


def favourites(request):
    """Allows to display the favourites of a user in the template"""
    userid = request.user.id
    user_favs = select_user_favs(userid)
    return render(
        request, "mes_aliments.html", {"favlist": user_favs}
    )


def unlike(request, unliked_id):
    """Adds a favourite to the database for a user"""
    if request.method == "POST":
        remove_user_fav(
            request.user.id, unliked_id
        )
        url = reverse("favourites")
        return HttpResponseRedirect(url)


def register(request):
    """Returns the register page"""
    return render(request, "register.html")


def account(request):
    """Returns the account page"""
    return render(request, "mon_compte.html")


"""You'll find the functions below """


def make_user(
        username,
        password,
        mail,
        user_first_name,
        user_last_name):
    """
    This easily creates a user
    thanks to the Django admin system.
    """
    user = User.objects.create_user(
        username=username,
        password=password,
        email=mail,
        first_name=user_first_name,
        last_name=user_last_name,
    )
    user.save()
    return user


def select_liked_in_products(liked_id):
    """
    This returns the entire row of the product that we
    want to add to favourites
    """
    product = models.Products.objects.get(
        idproduct=liked_id
    )
    return product


def select_user_favs(userid):
    """
    Returns the favourites rows of a specific user
    """
    user_favs = models.Favorites.objects.filter(
        userid=userid)
    return user_favs


def remove_user_fav(userid_unlike, unliked_id):
    """Removes a article from the user's favourites list"""
    unliked_product = models.Favorites.objects.get(
        userid=userid_unlike, productid=unliked_id
    )
    unliked_product.delete()
    return unliked_product

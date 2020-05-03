"""Create your views here."""

from foodfacts.models import Categories, Favorites, Products, Users
from foodfacts.modules.database_service import DatabaseService
from . import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NavSearchForm


def home(request):
    return render(request, "accueil.html")


def aliment(request):
    return render(request, "aliment.html")


def resultats(request):
    return render(request, "resultats.html")


def favourites(request):
    return render(request, "mes_aliments.html")


def account(request):
    return render(request, "mon_compte.html")


def notice(request):
    return render(request, "mentions_legales.html")


def research(request):
    form = NavSearchForm(request.POST)
    url = reverse("search_term", args=[form.get_search_term()])
    return HttpResponseRedirect(url)


def research_term(request, search_term):
    context = {}
    try:
        term_data = Products.objects.filter(productname=search_term).order_by("-nutrigrade")[0]
        context["product"] = term_data
        print(f"------------{term_data}-----------")

    except Exception as err:
        print("-------------------------NON TROUVÉ----------------------")

    try:
        better_products = DatabaseService.show_better_products_bis()
    except Exception as err:
        print("---------------------IMPOSSIBLE DE RECUPERER LES ALIMENTS DE REMPLACEMENT ---------------")


    return render(request, "resultats.html", context)



"""Create your views here."""

from foodfacts.models import Categories, Favorites, Products
from foodfacts.modules.database_service import DatabaseService

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NavSearchForm


def home(request):
    return render(request, "accueil.html")


def aliment(request, product_chosen):
    return HttpResponseRedirect(product_chosen)



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
        term_data = Products.objects.filter(productname=search_term).order_by("-nutrition_Score_100g")[0]
        context["product"] = term_data
        print(f"------------{term_data}-----------")
        try:
            better_products = DatabaseService.select_better_products(
                term_data.productname, term_data.category, term_data.nutrition_Score_100g)
            if better_products is not None and len(better_products) > 0:
                context["better"] = better_products
            else:
                context["better"] = None
        except Exception as err:
            print("---------------------IMPOSSIBLE DE RECUPERER LES ALIMENTS DE REMPLACEMENT ---------------")

    except Exception as err:
        print("-------------------------NON TROUVÉ----------------------")


    return render(request, "resultats.html", context)


def product_chosen(request, product_chosen):
    context = {}
    try:
        product = Products.objects.get(idproduct=product_chosen)
        context["product"] = product
    except Exception as err:
        print("---------------------IMPOSSIBLE DE RECUPERER CE PRODUIT ---------------")
    return render(request, "aliment.html", context)

def signin(request):
    return render(request, "signin.html")

def register(request):
    return render(request, "register.html")
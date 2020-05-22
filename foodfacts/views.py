"""Create your views here."""
from foodfacts.models import Products
from foodfacts.modules.database_service import DatabaseService
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NavSearchForm


def home(request):
    user = request.user
    print(user)
    return render(request, "accueil.html", {"user": user})


def aliment(request, product_chosen):
    return HttpResponseRedirect(product_chosen)


def resultats(request):
    return render(request, "resultats.html")


def notice(request):
    return render(request, "mentions_legales.html")


def research(request):
    form = NavSearchForm(request.POST)
    search_term = "empty"
    if form.is_valid():
        search_term = form.cleaned_data["nav_search"]
    url = reverse("search_term", args=[search_term])
    return HttpResponseRedirect(url)


def research_term(request, search_term):
    user_id = request.user.id
    context = {}
    try:
        term_data = DatabaseService.select_product(search_term)
        term_category = term_data.category
        term_name = term_data.productname
        term_score = term_data.nutrition_Score_100g

        context["product"] = term_data
        print(f"------------{term_data}-----------")
        try:
            better_products = DatabaseService.select_better_products(
                 term_category, term_score)
            relevant_favourites = DatabaseService.sort_favourites(user_id, term_category)
            favs_id_list = []
            for item in relevant_favourites:
                favs_id_list.append(item.productid)
            if better_products is not None and len(better_products) > 0:
                context["better"] = better_products
                context["favs"] = favs_id_list
            else:
                context["better"] = None
        except KeyError:
            print("---------------------IMPOSSIBLE DE RECUPERER LES ALIMENTS DE REMPLACEMENT ---------------")

    except KeyError:
        print("-------------------------NON TROUVÉ----------------------")

    return render(request, "resultats.html", context)


def product_chosen(request, product_chosen):
    context = {}
    try:
        product = Products.objects.get(idproduct=product_chosen)
        context["product"] = product
    except KeyError:
        print("---------------------IMPOSSIBLE DE RECUPERER CE PRODUIT ---------------")
    return render(request, "aliment.html", context)



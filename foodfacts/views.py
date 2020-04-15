"""Create your views here."""
from django.shortcuts import render
from django.http import HttpResponse


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
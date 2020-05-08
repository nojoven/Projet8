from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CreateForm


def create_user(request, product_chosen):
    form = CreateForm(request.POST)
    url = reverse("search_term", args=[form.get_search_term()])
    return HttpResponseRedirect(url)

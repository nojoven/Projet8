from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('aliment', views.aliment, name='aliment'),
    path('resultats', views.resultats, name='resultats'),
    path('favourites', views.favourites, name='favourites'),
    path('account', views.account, name='account'),
    path('notice', views.notice, name='notice'),
]
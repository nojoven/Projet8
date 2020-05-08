from . import views
from django.urls import path
from django.conf.urls import re_path


urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^resultats/?$', views.resultats, name='resultats'),
    path('aliment/<int:product_chosen>/', views.product_chosen, name='product_chosen'),
    path('resultats/<str:search_term>/', views.research_term, name='search_term'),
    re_path(r'^research/?$', views.research, name='research'),
    re_path(r'^favourites/?$', views.favourites, name='favourites'),
    re_path(r'^account/?$', views.account, name='account'),
    re_path(r'^notice/?$', views.notice, name='notice'),
    re_path(r'^signin/?$', views.signin, name='signin'),
    re_path(r'^register/?$', views.register, name='register'),

]

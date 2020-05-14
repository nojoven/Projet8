from . import views
from django.conf.urls import re_path
from django.urls import path



urlpatterns = [
    re_path(r'^create/?$', views.create_user, name='create'),
    re_path(r'^signin/?$', views.signin_user, name='signin'),
    re_path(r'^profileupdate/?$', views.update_profile, name='profileupdate'),
    re_path(r'^logout/?$', views.logout_user, name='logout'),
    re_path(r'^like/?$', views.like, name='like'),
    re_path(r'^unlike/?$', views.unlike, name='unlike'),
    re_path(r'^favourites/?$', views.favourites, name='favourites'),
]

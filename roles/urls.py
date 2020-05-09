from . import views
from django.conf.urls import re_path
from django.urls import path



urlpatterns = [
    re_path(r'^create/?$', views.create_user, name='create'),
    re_path(r'^signin/?$', views.signin_user, name='signin'),
    re_path(r'^profileupdate/?$', views.profile_update, name='signin'),
]

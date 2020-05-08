from . import views
from django.conf.urls import re_path




urlpatterns = [
    re_path(r'^create/?$', views.create_user, name='create'),
]

from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'authentification'
urlpatterns = [

    url(r'^$', views.log_in, name="log_in"),
    url(r'^deconnexion/$', views.log_out, name="log_out"),

]

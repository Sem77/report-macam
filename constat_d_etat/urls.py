from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'constat'
urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^searchartwork/', views.search_art_work, name="search_art_work"),
    re_path(r'^previsualisation/(?P<art_type>[_a-z]*)/(?P<art_work_id>[0-9]+)/$', views.preview_art_work, name="preview_art_work"),
    re_path(r'^liste_arts/(?P<art_type>[_a-z]*)/(?P<page_number>[0-9]+)/$', views.list_arts, name="list_arts"),

    url(r'^enregistrementoeuvre', views.save_art_work, name="save_art_work"),

    re_path(r'^(?P<art_type>[_a-z]*)/(?P<art_work_id>[0-9]*)/$', views.form_report, name="form_report"),

    re_path(r'^voir_constat/(?P<art_type>[_a-z]*)/(?P<art_work_id>[0-9]*)/(?P<report_id>[0-9]*)/$', views.show_report, name="show_report"),
    re_path(r'^pdf/(?P<art_type>[_a-z]*)/(?P<art_work_id>[0-9]*)/(?P<report_id>[0-9]*)/$', views.generate_pdf_file, name="generate_pdf_file"),

]

from django.contrib import admin
from django.urls import path
from . import views

app_name = "quotes_app"

urlpatterns = [
    path("", views.main, name='root'),
    path("add_quote/", views.add_quote, name='add_quote'),
    path("add_tag/", views.add_tag, name='add_tag'),
    path("add_author/", views.add_author, name='add_author'),
    path("quotes/", views.quotes, name='quotes')
]

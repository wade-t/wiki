from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageName>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("createPage", views.createPage, name="createPage"),
    path("editPage", views.editPage, name="editPage"),
    path("randomPage", views.randomPage, name="randomPage")
]

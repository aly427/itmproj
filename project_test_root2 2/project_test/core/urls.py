from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"), 
path("<str:name>", views.index, name = "index"),
path("create/", views.create, name = "create"),
path("<str:name>/<int:id>", views.flashcard, name = "flashcard")


]
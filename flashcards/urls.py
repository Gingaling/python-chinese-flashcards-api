from django.urls import path

from flashcards.views import (
    home,
    create,
    delete,
    FlashcardListView, FlashcardCreateView
)

from .models import Flashcard

urlpatterns = [
    path(
        "",
        home,
        name='home',
    ),
    path(
        'home/',
        home,
        name='home',
    ),
    path(
        "list/",
        FlashcardListView.as_view(), 
        name = "flashcard_list"
    ),
    path(
        "add/",
        create,
        name="create"
    ),
    path(
        "create/",
        create,
        name="create"
    ),
    path(
        'delete/<int:id>',
        delete,
        name="delete"
    ),
    path(
        "*",
        home,
        name="home"
    ),
]
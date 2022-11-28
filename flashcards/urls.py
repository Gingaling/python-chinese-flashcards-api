from django.urls import include, path

from . import views

from flashcards.views import (
    home,
    create,
    collection,
    delete,
    FlashcardListView,
    FlashcardCreateView,
    # FlashcardUpdateView,
)

from .models import Flashcard

urlpatterns = [
    path(
        'home/',
        home,
        name='home',
    ),
    path(
        "",
        FlashcardListView.as_view(),
        name="Flashcard-list",
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
    # path(
    #     "edit/<int:pk>",
    #     FlashcardUpdateView.as_view(),
    #     name="Flashcard-update"
    # ),
    path(
        'delete/<int:id>',
        delete,
        name="delete"
    ),
]
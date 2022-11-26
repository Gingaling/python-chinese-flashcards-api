from django.urls import path, include, reverse_lazy
# from . import views
from flashcards.views import (
    home,
    create,
    delete,
    FlashcardListView, FlashcardCreateView
)

from .models import Flashcard

urlpatterns = [
    path(
        'home',
        home,
        name='home',
    ),
    path(
        "",
        FlashcardListView.as_view(),
        name="flashcard_list_1",
    ),
    path(
        "list/",
        FlashcardListView.as_view(), 
        name = "flashcard_list"
    ),
    path(
        "new/",
        FlashcardCreateView.as_view(),
        name="flashcard-create"
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
]
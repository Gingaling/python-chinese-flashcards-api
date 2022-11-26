# from django.views.generic import ListView

# from django.shortcuts import (
#     redirect,
#     render,
#     get_object_or_404
# )

# from django.urls import (
#     reverse,
#     reverse_lazy
# )

# from flashcards.models import Flashcard
# from .models import FlashcardFORM

# def home(request):
#     queryset = Flashcard.objects.all().order_by('-date_created')
#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'flashcards/base.html', context)


# def create(request):
#     form = FlashcardFORM(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('http://localhost:8000')
#     context = {
#         "form": form
#     }
#     return render(request, 'flashcards/createform.html', context)

# def delete(request, id):
#     data = get_object_or_404(Flashcard, id=id)
#     data.delete()
#     return render(request, 'http://localhost:8000')

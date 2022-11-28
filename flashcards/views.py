from django.urls import (
    reverse,
    reverse_lazy
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404
)

from .models import Flashcard
from .forms import FlashcardFORM

class FlashcardListView(ListView):
    model = Flashcard
    queryset = Flashcard.objects.all().order_by("difficulty", "-date_created")
    
class FlashcardCreateView(CreateView):
    model = Flashcard
    fields = ['difficulty', 'question', 'pinyin', 'answer', 'mnemonic']
    success_url = reverse_lazy('create')
    
# class FlashcardUpdateView(FlashcardCreateView, UpdateView):
#     success_url = reverse("Flashcard-list")
    
def home(request):
    return render(request, 'flashcards/home.html', {})

def collection(request):
    queryset = Flashcard.objects.all().order_by('-date_created')
    context = {
        'queryset': queryset
    }
    return render(request, 'flashcards/base.html', context)

def create(request):
    form = FlashcardFORM(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000')
    # context = {
    #     "form": form
    # }``
    else:
        form = FlashcardFORM()
    return render(request, 'flashcards/createform.html', {'form': form})


def delete(request, id):
    data = get_object_or_404(Flashcard, id=id)
    data.delete()
    return redirect('http://localhost:8000')
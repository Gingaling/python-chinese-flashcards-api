from django import forms
from .models import Flashcard

class FlashcardFORM(forms.ModelForm):
    difficulty = forms.IntegerField(widget=forms.NumberInput
    (attrs={
        'type': "integer",
        "class": "form-control",
        "placeholder": "difficulty"
    }))
    question = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "question"
    }))
    pinyin = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "pinyin"
    }))
    answer = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "answer"
    }))
    mnemonic = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "mnemonic"
    }))

    class Meta:
        model = Flashcard
        fields = [
            'difficulty',
            'question',
            'answer',
            'mnemonic',
        ]

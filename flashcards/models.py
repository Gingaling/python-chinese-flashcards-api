from django.db import models

class Flashcard(models.Model):
    difficulty = models.IntegerField(default=1)
    question = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100, default="--")
    answer = models.CharField(max_length=100)
    mnemonic = models.CharField(max_length=100, blank=True)
    box = models.IntegerField(default=1, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
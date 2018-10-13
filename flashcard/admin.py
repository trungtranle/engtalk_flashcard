from django.contrib import admin
from flashcard.models import Word, Writing, Writing_question
# Register your models here.
admin.site.register(Word)
admin.site.register(Writing)
admin.site.register(Writing_question)
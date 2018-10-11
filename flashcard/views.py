from django.shortcuts import render
from flashcard.forms import WordForm
from flashcard.models import Word
from random import randint
# Create your views here.


def index(request):
    count = Word.objects.count()
    id_ = randint(1, count-1)
    word = Word.objects.get(pk = id_)
 
    return render(request, 'index.html', {"word":word})

def add_word(request):
    saved = False
    if request.method == "POST":
        form = WordForm(data = request.POST)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = WordForm
    return render(
        request, 
        'add.html',
        {'form':form,
        'saved':saved})

def list_word(request):
    word_list = Word.objects.all()

    return render(request, 'list.html', {'word_list':word_list})


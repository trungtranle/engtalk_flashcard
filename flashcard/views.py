from django.shortcuts import render
from flashcard.forms import WordForm
from flashcard.models import Word
# Create your views here.
def index(request):
    return render(request, 'index.html')

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
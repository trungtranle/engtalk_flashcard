from django import forms
from flashcard.models import Word, Writing

class WordForm(forms.ModelForm):
    part_of_speech = forms.ChoiceField(choices=(('noun', 'noun'), ('pronoun', 'pronoun'), ('adjective', 'adjective'),('verb', 'verb'), ('adverb', 'adverb'), ('preposition','preposition'),('conjunction', 'conjunction'),('interjection', 'interjection')))
    
    class Meta:
        model = Word
        fields = "__all__"

class WritingForm(forms.ModelForm):
    question = forms.CharField(widget = forms.HiddenInput())
    class Meta:
        model = Writing
        fields = "__all__"
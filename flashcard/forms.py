from django import forms
from flashcard.models import Word
class WordForm(forms.ModelForm):
    part_of_speech = forms.ChoiceField(choices=(('noun', 'noun'), ('pronoun', 'pronoun'), ('adjective', 'adjective'),('verb', 'verb'), ('adverb', 'adverb'), ('preposition','preposition'),('conjunction', 'conjunction'),('interjection', 'interjection')))
    
    class Meta:
        model = Word
        fields = "__all__"
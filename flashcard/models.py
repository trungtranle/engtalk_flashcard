from django.db import models

# Create your models here.
class Word(models.Model):
    user = models.CharField(max_length = 40)
    word = models.CharField(max_length = 50, unique = True)
    part_of_speech = models.CharField(max_length = 50)
    definition = models.TextField()
    example = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)
	
    def __str__(self):
        return self.word

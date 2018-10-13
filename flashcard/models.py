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
class Writing_question(models.Model):
    task = models.PositiveIntegerField()
    question = models.TextField()
    picture = models.ImageField(upload_to = 'img/')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.added.strftime("%Y-%m-%d")
class Writing(models.Model):
    user = models.CharField(max_length = 40)
    question = models.ForeignKey(Writing_question, on_delete = models.PROTECT)
    essay = models.TextField()
    added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user

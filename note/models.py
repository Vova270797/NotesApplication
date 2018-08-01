from django.db import models

# Create your models here.

class Note(models.Model):

    text = models.TextField("Текст нотатки")
    number_of_unique = models.IntegerField(default=0)

    def __str__(self):
        if len(self.text) < 20 :
            return self.text
        else:
            return  self.text[0:20] + "..."

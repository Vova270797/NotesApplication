from django.db import models

# Create your models here.

class Note(models.Model):
    ''' Клас заміток
    '''

    text = models.TextField("Текст нотатки")
    created = models.DateTimeField("Дата створення", auto_now_add=True)

    class Meta:
        verbose_name = "Нотатка"
        verbose_name_plural = "Нотатки"

    def __str__(self):
        if len(self.text) < 20 :
            return self.text
        else:
            return  self.text[0:20] + "..."

from django.db import models


class Note(models.Model):
    text = models.TextField(
        max_length=8000, blank=True, null=True,
        verbose_name='Note text'
    )
    number_of_unique = models.IntegerField(
        default=0,
        verbose_name='Number of unique words'
    )

    def __str__(self):
        if len(self.text) < 20:
            return self.text
        else:
            return self.text[0:20] + "..."

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Note'

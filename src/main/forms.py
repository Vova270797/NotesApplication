from django.forms import ModelForm

from main.models import Note


class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text',)

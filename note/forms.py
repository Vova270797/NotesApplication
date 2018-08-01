from django.forms import ModelForm
from .models import Note

class NotesForm(ModelForm):

    class Meta:
        model = Note
        fields = ('text',)
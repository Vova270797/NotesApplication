from django.shortcuts import render, redirect
from note.models import Note
from note.forms import NotesForm

# Create your views here.

def note_list(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect(note_list)
    else:
        form = NotesForm()
    return render(request, "note/note_list.html",
                  {"notes": notes,
                   "form": form})

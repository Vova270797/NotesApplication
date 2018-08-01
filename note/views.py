from django.shortcuts import render, redirect
from note.models import Note
from note.forms import NotesForm
from django.views.generic import View
# Create your views here.


class Home(View):

    def get(self, request):
        note_list = Note.objects.all().order_by("-number_of_unique")
        form = NotesForm()
        context = {"note_list": note_list, "form": form}

        return render(request,  "note/note_list.html", context)

    def post(self, request):
        form = NotesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.number_of_unique = len(set(form.text.split()))
            form.save()
            return redirect("home")
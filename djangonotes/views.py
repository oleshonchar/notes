from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/post_show.html', {'notes': notes})


def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/post_add.html', {'form': form})

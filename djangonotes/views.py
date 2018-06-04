from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect


def note_list(request):
    notes = Note.objects.all().order_by('-unique_words')
    return render(request, 'notes/post_show.html', {'notes': notes})


def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        text = form.data['text']
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
        text = text.lower()
        words = text.split()
        unique_words = list()
        for word in words:
            if word in unique_words:
                pass
            else:
                unique_words.append(word)

        if form.is_valid():
            note = form.save(commit=False)
            note.unique_words = len(unique_words)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/post_add.html', {'form': form})

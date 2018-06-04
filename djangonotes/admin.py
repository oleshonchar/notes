from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Note._meta.fields]

    class Meta:
        model = Note


admin.site.register(Note, NoteAdmin)

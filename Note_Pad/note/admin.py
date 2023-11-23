from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created', 'updated')
    search_fields = ('title', 'created')
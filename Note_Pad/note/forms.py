from django import forms
from .models import Note
class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body', 'is_pin')

class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body', 'is_pin')
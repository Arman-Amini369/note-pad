from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteCreateForm, NoteEditForm
from datetime import datetime
from django.http import HttpResponse

def index(request):
    notes = Note.objects.all()
    return render(request, "note/index.html", {"notes" : notes})

@login_required
def detail(request, note_id):
    notes = Note.objects.filter(id=note_id)
    return render(request, "note/detail.html", {"notes" : notes})

@login_required
def create(request):
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Note.objects.create(user = request.user, title = cd["title"], body = cd["body"], is_pin = cd["is_pin"])
            messages.success(request, "Note Created Successfully", 'success')
            return redirect('note:home')
    else:
        form = NoteCreateForm()
    return render(request, "note/create.html", {"form" : form})

@login_required
def delete(request, note_id):
    note = Note.objects.filter(id=note_id).delete()
    messages.success(request, "Note Deleted Successfully", 'success')
    return redirect('note:home')

@login_required
def edit(request, note_id):
    notes = Note.objects.get(id=note_id)
    if request.method == "POST":
        form = NoteEditForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            notes.updated = datetime.now()
            messages.success(request, "Note Edited Successfully", 'success')
            return redirect('note:detail', note_id)
    else:
        form = NoteEditForm(instance=notes)
    return render(request, "note/edit.html", {"form" : form})


def error_404(request, exception):
        return render(request,'404.html', status = 404)

def contact(request):
    return render(request, "note/contact.html")

@login_required
def user_info(request):
    return render(request, "note/user.html")
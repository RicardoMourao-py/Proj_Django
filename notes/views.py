from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        note=Note()
        title=request.POST.get('title')
        content=request.POST.get('content')
        note.title=title
        note.content=content
        note.save()
        return redirect('index')
    else:
        allNotes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': allNotes})

def delete(request, id):
    note=Note.objects.get(id=id)
    note.delete()
    return redirect('index')

def edita(request,id):    
    Note.objects.filter(id=id).update(title=request.POST.get('title'), content=request.POST.get('content'))
    return redirect('index')

from django.shortcuts import render , get_object_or_404, redirect
from .models import SecretNote

# 1. Page to create the note
def create_note(request):
    if request.method == "POST":
        content_data = request.POST.get("content")
        #SecretNote.objects.create(content=content_data)
        #return redirect('success_page')
        new_note = SecretNote.objects.create(content=content_data)
        return render(request, 'notes/created.html', {'note_id': new_note.id})
    return render(request, 'notes/home.html')

# 2. Page to view and DELETE the note
def view_note(request, note_id):
    note = get_object_or_404(SecretNote, id=note_id)
    content = note.content # Save content to memory
    note.delete()          # Delete from Database immediately
    return render(request, 'notes/view.html', {'content': content})

def index(request):
    return render(request, 'notes/index.html')

def home(request):
    return render(request, 'notes/home.html')
# Create your views here.

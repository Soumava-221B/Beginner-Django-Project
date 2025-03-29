from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.db.models import Exists, OuterRef

from .models import Note, Like
from .forms import LikeForm

class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.annotate(liked=Exists(Like.objects.filter(liker=user, note=OuterRef('pk'))))
        return queryset    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LikeForm
        return context
    
    
class NotesDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/notes_detail.html"


    
def like(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'POST':
        like_object = Like.objects.filter(liker=request.user, note=note)
        if like_object.exists():
            like_object.delete()
        else:
            form = LikeForm(request.POST)
            if form.is_valid():
                form.instance.liker = request.user
                form.instance.note = note
                form.save()         
    return redirect('notes_list')
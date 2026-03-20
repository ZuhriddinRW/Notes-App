from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note


def welcome(request):
    return render(request, "index.html")


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes.html'
    ordering = '-created_at'
    context_object_name = 'notes'
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteAddView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'add.html'
    fields = ['title', 'content', 'color']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View, UpdateView
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
        return Note.objects.filter(user=self.request.user, is_archived=False)


class ArchivedNotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'archived.html'
    ordering = '-created_at'
    context_object_name = 'notes'
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user, is_archived=True)


class NoteAddView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'add.html'
    fields = ['title', 'content', 'color']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'update.html'
    fields = ['title', 'content', 'color']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteArchiveView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.is_archived = not note.is_archived
        note.save()
        return redirect('notes')


class NoteDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.delete()
        return redirect('archived')

from django.urls import path
from .views import *


urlpatterns = [
    path("", welcome, name="welcome"),
    path("notes/", NotesListView.as_view(), name="notes"),
    path("notes/archived", ArchivedNotesListView.as_view(), name="archived"),
    path("notes/add", NoteAddView.as_view(), name="add"),
    path("notes/<int:pk>/update", NoteUpdateView.as_view(), name="update"),
    path("notes/<int:pk>/delete", NoteDeleteView.as_view(), name="delete"),
    path("notes/<int:pk>/archive", NoteArchiveView.as_view(), name="archive"),
]
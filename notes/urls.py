from django.urls import path
from .views import *


urlpatterns = [
    path("", welcome, name="welcome"),
    path("notes/", NotesListView.as_view(), name="notes"),
    path("notes/add", NoteAddView.as_view(), name="add"),
]
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="api-register"),
    path("login/", TokenObtainPairView.as_view(), name="api-login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="api-token-refresh"),

    path("notes/", NoteListCreateView.as_view(), name="api-note-list-create"),
    path("notes/archived/", ArchivedNoteListView.as_view(), name="api-archived-note-list"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="api-note-detail"),
    path("notes/<int:pk>/archive-toggle/", NoteArchiveToggleView.as_view(), name="api-note-archive-toggle"),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
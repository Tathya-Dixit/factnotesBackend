from django.urls import path
from api.views import NoteApiView,NotesApiView

urlpatterns = [
    path('notes/',NotesApiView.as_view()),
    path('notes/<str:pk>/', NoteApiView.as_view())
]




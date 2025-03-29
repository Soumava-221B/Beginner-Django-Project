from django.urls import path

from . import views

urlpatterns = [
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes_details"),
    path('note/like/<int:pk>', views.like, name='like'),
    path('notes_list', views.NotesListView.as_view(), name="notes_list"),
]
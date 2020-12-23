from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as api_views

urlpatterns = [
    path('', api_views.NoteListView.as_view()),
    path('<int:pk>/', api_views.NoteView.as_view()),
    path('create/', api_views.NoteCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
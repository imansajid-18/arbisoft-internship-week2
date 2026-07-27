from rest_framework import viewsets

from crud_rest_api.models import Note
from crud_rest_api.serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

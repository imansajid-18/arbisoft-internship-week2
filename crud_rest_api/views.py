from rest_framework import viewsets

from crud_rest_api.models import Notes
from crud_rest_api.serializers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


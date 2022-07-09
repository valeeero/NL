from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import NoteList
from .serializers import NoteSerializer


def notes_page(request):
    return render(request, 'base.html', {'notes': NoteList.objects.all()})


class NoteView(ModelViewSet):
    queryset = NoteList.objects.all()
    serializer_class = NoteSerializer


def notes_app(request):
    return render(request, 'mane_app.html')

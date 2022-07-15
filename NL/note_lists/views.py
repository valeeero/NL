from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import NoteList
from .serializers import NoteSerializer


def notes_page(request):
    return render(request, 'base.html', {'notes': NoteList.objects.all()})


class NoteView(ModelViewSet):
    queryset = NoteList.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['text', 'header']
    oredering_fields = ['id', 'header']


def notes_app(request):
    return render(request, 'mane_app.html')

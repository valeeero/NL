from django.db import models


class NoteList(models.Model):
    text = models.TextField()
    date = models.DateTimeField()

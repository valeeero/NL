from django.db import models


class NoteList(models.Model):
    header = models.CharField(max_length=50, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ID - {self.id}: {self.header}'

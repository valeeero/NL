from rest_framework.serializers import ModelSerializer

from .models import NoteList


class NoteSerializer(ModelSerializer):
	class Meta:
		model = NoteList
		fields = ['text', 'date', ]

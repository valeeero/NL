from django.contrib import admin
from django.urls import path

from rest_framework.routers import SimpleRouter

from note_lists.views import NoteView, notes_page

from note_lists.views import notes_app

router = SimpleRouter()
router.register('note_lists', NoteView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', notes_page),
    path('note_page/', notes_app),
]

urlpatterns += router.urls

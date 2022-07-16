from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from note_lists.views import NoteView, notes_page

from note_lists.views import notes_app

router = SimpleRouter()
router.register('note_lists', NoteView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', notes_page),
    path('note_page/', notes_app),
    # url('social/', include('social_django.urls', namespace='social')),
]


urlpatterns += router.urls

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('',views.index, name='home'),
   path('artist/<int:id>/',views.artist,name='artist'),
   path('base',views.base, name='base'),
   path('upload',views.upload, name='upload'),
   path('add_song',views.add_song,name='add'),
   path('song/<int:uid>/',views.song.as_view(),name='song-data'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

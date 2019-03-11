from django.urls import path,re_path
from . import views

app_name = 'Songlutter'

# /Songlutter/
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #/Songlutter/123/
    re_path(r'(?P<pk>[0-9]+)',views.DetailView.as_view(),name='detail'),
    #Songlutter/create-album/
    path('album/create/',views.CreateAlbum.as_view(),name='create-album'),
    # Songlutter/update-album/
    re_path(r'album/(?P<pk>[0-9]+)',views.UpdateAlbum.as_view(),name='update-album'),
    # Songlutter/delete-album/
    re_path(r'album/(?P<pk>[0-9]+)/delete/',views.delete,name='delete-album'),
    ]

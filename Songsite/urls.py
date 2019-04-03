from django.urls import path,re_path
from . import views

app_name = 'Songlutter'

# /Songlutter/
urlpatterns = [
    path('home',views.IndexView.as_view(),name='index'),
    #/Songlutter/123/
    re_path(r'(?P<pk>[0-9]+)/',views.DetailView.as_view(),name='detail'),
    #Songlutter/create-album/
    path('album/create/',views.AlbumCreate.as_view(),name='album-create'),
    # Songlutter/update-album/
    re_path(r'(?P<pk>[0-9]+)/update',views.AlbumUpdate.as_view(),name='album-update'),
    # Songlutter/delete-album/
    re_path(r'(?P<pk>[0-9]+)/delete/',views.AlbumDelete.as_view(),name='album-delete'),
    #
    path('',views.UserFormView.as_view(),name='register'),
]

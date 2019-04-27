from django.urls import path,re_path
from . import views

app_name = 'Songlutter'

# /Songlutter/
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),

    # songs list
    path('allsongs/',views.AllSongs.as_view(),name='all-songs'),

    #123/
    re_path(r'(?P<pk>[0-9]+)/',views.DetailView.as_view(),name='detail'),
    #create-album/
    path('album/create/',views.AlbumCreate.as_view(),name='album-create'),
    #update-album/
    re_path(r'(?P<pk>[0-9]+)/update/',views.AlbumUpdate.as_view(),name='album-update'),
    #delete-album/
    re_path(r'(?P<pk>[0-9]+)/delete/',views.AlbumDelete.as_view(),name='album-delete'),
    #
    path('register/',views.register.as_view(),name='register'),
    #
    path('login/',views.loginUser.as_view(),name='login'),

    # logout/
    # path('logout/',views.logoutUser.as_view(),name='logout')
    #
    # re_path(r'(?P<song_id>[0-9]+)/favorited/',views.songFavorite,name='song-favorite'),
]

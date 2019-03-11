from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'Songlutter/home.html'
    context_object_name = 'playlists'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'Songlutter/songs.html'

class favorite():
        pass


class CreateAlbum(CreateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('Songlutter:index')


def delete(request,pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request,'Songlutter:index',{"album":albums})

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from .models import Album,Song

class IndexView(generic.ListView):
    template_name = 'Songlutter/home.html'
    context_object_name = 'playlists'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'Songlutter/songs.html'


class AllSongs(generic.ListView):
    template_name = 'Songlutter/allsongs.html'
    context_object_name = 'songslist'

    def get_queryset(self):
        return Song.objects.all()



class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']



class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']



class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('Songlutter:index')




class register(View):
    form_class = UserForm
    template_name = "Songsite/registration_form.html"

    #Display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #Display processed form
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)


            #clean (NORMALIZE) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()


            # return user object if credentials are correct
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Songlutter:index')

        return render(request, self.template_name, {'form': form})

class loginUser(View):
    template_name = 'Songsite/login.html'

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('Songlutter:index')


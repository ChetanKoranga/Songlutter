from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
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



class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']



class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title','album_artist','genre','album_logo']



class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('Songlutter:index')




class UserFormView(View):
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
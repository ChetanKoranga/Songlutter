from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=500)
    album_artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(max_length=1000)

    def get_absolute_url(self):
        return reverse('Songlutter:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title+" ("+self.album_artist+")"

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title+"."+self.file_type

from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=250)
    album_genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=200)

    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=200)
    is_favorite = models.BooleanField(max_length=200)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song_title

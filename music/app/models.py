from django.db import models




class Song(models.Model):
    song_name=models.CharField(max_length=51)
    singer_name=models.CharField(max_length=50)
    song_image=models.ImageField(upload_to='image')
    song_audio=models.FileField(upload_to='song')
    upload_time=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.song_name

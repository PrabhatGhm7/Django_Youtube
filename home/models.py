from django.conf import settings
from django.db import models
import PIL
class video_upload(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_upload = models.DateField(auto_now_add=True)
    video = models.FileField(upload_to='media')
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title

class channel(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    video = models.ForeignKey(video_upload , on_delete=models.CASCADE)

class comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    video = models.ForeignKey(video_upload, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    
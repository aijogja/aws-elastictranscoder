from django.db import models
import uuid
import os

# Create your models here.

def get_video_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('video', filename)

class Video(models.Model):
    # name = models.CharField(max_length=255, null=True)
    video = models.FileField(upload_to=get_video_file_path, max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Video"

    # def __unicode__(self):
        # return self.video

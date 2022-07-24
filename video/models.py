from django.db import models
from .validators import file_size,validate_file_extension,file_length

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=250)
    video = models.FileField(upload_to="video/%y",validators=[file_size,validate_file_extension,file_length])
    dateofupload = models.DateField(null=True)
    # videofcharge = models.FloatField()

    def __str__(self):
        return "caption"

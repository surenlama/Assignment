from pyexpat import model
from django.db import models
from .validators import file_size,validate_file_extension,file_length
from django.contrib.auth.models import User

#Video model
class Video(models.Model):
    caption = models.CharField(max_length=250)
    video = models.FileField(upload_to="video/%y",validators=[file_size,validate_file_extension,file_length])
    dateofupload = models.DateField(null=True)
    createdby = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.caption

#Comment model
class Comment(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

from rest_framework.generics import CreateAPIView, ListAPIView
from video.models import Video
from .serializer import VideoSerializer,VideoListSerializer,CommentSerializer
# from rest_framework.authentication import SessionAuthentication
import datetime
from rest_framework.permissions import IsAuthenticated
from video.models import Comment
import moviepy.editor
from django.contrib import messages
from django.core.exceptions import ValidationError


#converting function
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

#Created video and  perform_create function will provide totalprice
class VideoCreateAPi(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    #showing total price
    def perform_create(self, serializer):
        obj =serializer.save(createdby=self.request.user)
        charges=0
        video = moviepy.editor.VideoFileClip("/home/suren/Desktop/suren/assignment/media/video/LAURE Ft. AIDRAY-ROHIT SHAKYA - Dui Rupaiyan [OFFICIAL MOVIE SONG](1).mp4")
        video_duration = int(video.duration)
        hours, mins, secs = convert(video_duration)     
        print("Hours:", hours)
        print("Minutes:", mins)
        print("Seconds:", secs)   
        filesize = obj.video.size
        if filesize<4194304000:
            charges+=5
        elif filesize>4194304000:  
            charges+=12.5
        if mins<6:
            charges+=12.5
        elif mins==6 and secs<16:
            charges+=12.5
        elif mins>6 :
            charges+=20
        elif mins==6 and secs>16:
            charges+=20    
        else:
            pass
        print(charges)
        messages.info(self.request, f'Your total charges {charges}') 


#Video will display accoring to the date of upload   
class VideoListAPi(ListAPIView):
    queryset =   Video.objects.filter(dateofupload__lte=datetime.datetime.now().date())
    serializer_class = VideoListSerializer
    permission_classes = [IsAuthenticated]

    
#Create comment of the video(Additional feature)   
class CommentCreateAPi(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated] 


#List comment of the video(Additional feature)
class CommentListAPi(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

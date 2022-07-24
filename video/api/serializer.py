from rest_framework import serializers
from video.models import Video
from django.core.exceptions import ValidationError
import moviepy.editor
from django.contrib import messages


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "caption",
            "video",
            "dateofupload",
        ]


    def validate_video(self,value):
        charges=0
        video = moviepy.editor.VideoFileClip("/home/suren/Desktop/suren/project/media/video/22/LAURE_Ft._AIDRAY-ROHIT_SHAKYA_-_Dui_Rupaiyan_OFFICIAL_MOVIE_SONG1_dKnOigV.mp4")
        # Contains the duration of the video in terms of seconds
        video_duration = int(video.duration)
        hours, mins, secs = convert(video_duration)     
        print("Hours:", hours)
        print("Minutes:", mins)
        print("Seconds:", secs)


        filesize = value.size
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
        raise ValidationError(f"Your total charge is:{charges}")


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "caption",
            "video",
            "dateofupload",
        ]

        # print(file_size)
            # if filesize>10000000:
            #     print('yes')
            #     raise ValidationError("maximum size is 500 mb")  
            # else:
            #     print('sorry not')         
            # return value
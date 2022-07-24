from rest_framework import serializers
from video.models import Video,Comment
from django.core.exceptions import ValidationError
from django.contrib import messages




class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "caption",
            "video",
            "dateofupload",
            
        ]



class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "caption",
            "video",
            "dateofupload",
            
        ]

 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "video",
            "date",
            "user",
            "comment"
        ]
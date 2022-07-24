from django.core.exceptions import ValidationError
import moviepy.editor
from django.contrib import messages


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds


def file_length(value):
    video = moviepy.editor.VideoFileClip("/home/suren/Desktop/suren/project/media/video/22/LAURE_Ft._AIDRAY-ROHIT_SHAKYA_-_Dui_Rupaiyan_OFFICIAL_MOVIE_SONG1_dKnOigV.mp4")
    # Contains the duration of the video in terms of seconds
    video_duration = int(video.duration)
    hours, mins, secs = convert(video_duration)
  
    if mins>10:
        raise ValidationError("maximum length of video should be 10")


def file_size(value):
    filesize = value.size
    # print(file_size)
    if filesize>8589934592:
        raise ValidationError("maximum size is 1 gb")

def validate_file_extension(value):
    if not value.name.endswith(".mp4") or  value.name.endswith(".mkv"):
        raise ValidationError("Only mp4 or mkv videos are accepted")


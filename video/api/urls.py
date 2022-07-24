from django.urls import path

from video.api.views import VideoCreateAPi,VideoListAPi,CommentListAPi,CommentCreateAPi

app_name = "video-api"


urlpatterns = [
    path(
        "video/create/",
        VideoCreateAPi.as_view(),
        name="video-create",
    ),
    path(
        "video/list/",
        VideoListAPi.as_view(),
        name="video-list",
    ),
  path(
        "comment/create/",
        CommentCreateAPi.as_view(),
        name="comment-create",
    ),
    path(
        "comment/list/",
        CommentListAPi.as_view(),
        name="comment-list",
    ),
    
  
]

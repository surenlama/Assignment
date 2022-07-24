from django.urls import path

from video.api.views import VideoCreateAPi,VideoListAPi

app_name = "video-api"


urlpatterns = [
    path(
        "create/",
        VideoCreateAPi.as_view(),
        name="video-create",
    ),
    path(
        "list/",
        VideoListAPi.as_view(),
        name="video-list",
    ),

]

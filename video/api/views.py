from rest_framework.generics import CreateAPIView, ListAPIView
from video.models import Video
from .serializer import VideoSerializer,VideoListSerializer
# from rest_framework.authentication import SessionAuthentication
import datetime
from rest_framework.permissions import IsAuthenticated


class VideoCreateAPi(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     obj = serializer.save()
    #     print(obj.video)
    #     serializer.save(profile=self.request.user.user_profile)


class VideoListAPi(ListAPIView):
    queryset =   Video.objects.filter(dateofupload__lte=datetime.datetime.now().date())
    serializer_class = VideoListSerializer
    permission_classes = [IsAuthenticated]

 
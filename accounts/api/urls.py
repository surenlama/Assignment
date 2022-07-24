from django.urls import path

from accounts.api.views import  UserCreateAPIView,UserListAPIView

app_name = "account-api"

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="create"),
    path("list/", UserListAPIView.as_view(), name="list"),
  
]
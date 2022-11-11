from django.urls import path

from .views import HomePageView, CreatePostView

urlpatterns = [
    path("posthome/", HomePageView.as_view(), name="posthome"),
    path("post/", CreatePostView.as_view(), name="post")
]
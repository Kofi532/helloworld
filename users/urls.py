from django.urls import path
from . import views
from .views import BasePageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns






urlpatterns = [
    path("base/", BasePageView.as_view(), name="base"),




]



from django.urls import path
from . import views
from .views import HoPageView


app_name = "blog"   


urlpatterns = [
    path("see/", HoPageView.as_view(), name="see"), 

    path("", views.register_request, name="register"),
 #   path("login/", views.login_request, name="login"),
]
# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, ServicePageView, PrefectPageView, GreatePostView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"), 
    path("home/", GreatePostView.as_view(), name="home"),
    path("service/", ServicePageView.as_view(), name="service"),
    path("prefects/", PrefectPageView.as_view(), name="prefects"),
    
]


    

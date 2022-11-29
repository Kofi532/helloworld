from unicodedata import name
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
from pathlib import Path
import ctypes  # An included library with Python install.
from .models import Post
from django.urls import reverse_lazy  
from .forms import PostForm, Clubs, Sports
from django.views.generic import ListView, CreateView
from django import forms
from posts.models import Post as Kk
from .models import Clubm, Sportm
from posts.views import headmistress, clubs_prefect, sports_prefect
from django.template import RequestContext
import requests
from django.contrib.auth.models import User
from datetime import datetime

class GalleryPageView(TemplateView):
    template_name = "gallery.html"


class GreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "index.html"
    success_url = '/'






def home_and_create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        form.save()
    else:
        form = PostForm()
    
    i = len(Kk.objects.all().filter(approve='yes'))
    ii = len(Clubm.objects.all().filter(approve='yes'))
    iii = len(Sportm.objects.all().filter(approve='yes'))

    check1 = Kk.objects.all().filter(approve='yes')[i-1]
    check2 = Kk.objects.all().filter(approve='yes')[i-2]
    check3 = Kk.objects.all().filter(approve='yes')[i-3]
    club1 = Clubm.objects.all().filter(approve='yes')[ii-1]
    sport1 = Sportm.objects.all().filter(approve='yes')[iii-1]


    return render(request, 'index.html', {'form': form, 'check1': check1, 'check2': check2 , 'check3': check3, 'club1': club1, 'sport1': sport1 })




class SportsView(CreateView):
    model = Sportm
    form_class = Sports
    template_name = "sports.html"
    success_url = "/we/"




class ClubsView(CreateView): 
    model = Clubm
    form_class = Clubs
    success_url = "/we/"
    template_name = "clubs.html"
    #template_name = "clubs.html"


    


class PrefectPageView(TemplateView):
    template_name = "prefects.html"


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):  # new
    template_name = "about.html"

class ServicePageView(TemplateView):
    template_name = "calenda.html"


class HoPageView(TemplateView):
    template_name = "your-name.html"

def uploadImg(request):
    
    image_list=[]

    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for file in files:
            image_list.append(file)
    return render(request, 'your-name.html',{'brands': image_list})



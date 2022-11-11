from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post, Experience, Post_a
from django.urls import reverse_lazy  # new

from django.views import generic
from .forms import PostForm, ApproveForm

class HomePageView(ListView):
    model = Post
    template_name = "posthome.html"
    success_url = reverse_lazy("home.html")

class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = "/"

class ApprovalPostView(CreateView):  # new
    model = Post_a
    form_class = ApproveForm
    template_name = "post.html"
    success_url = "/"

class List(generic.ListView):
    model = Experience
    template_name = 'posthome.html'
    queryset = Experience.objects.all()



# Create your views here.
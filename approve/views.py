from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm, Post
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from posts.models import Post as Pop
from django.http import HttpResponse
from django.template import loader
#from users.models import Post


class ApprovePostView(UserPassesTestMixin, CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "approval.html"
    success_url = "/"  
    def test_func(self):
        return self.request.user.is_superuser

def testing(request):
  c = Pop.objects.all()
  all_posts = Post.objects.all()
  template = loader.get_template('approval.html')
  context = {
    'all_posts': all_posts,
    'c': c,
  }
  return HttpResponse(template.render(context, request))

def a_view(request):
    
    all_posts = Post.objects.all()
    return render(request, "head.html", {'all_posts': all_posts})
